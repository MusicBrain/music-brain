__all__ = ['convert_psds', 'get_peaks', 'get_power', 'get_unit_label']

import numpy as np
import scipy
from .constants import *

def convert_psds(psds, dB=False, estimate='power', unit='µV'):
    psds = psds.copy()
    if estimate == 'auto':
        estimate = 'power' if dB else 'amplitude'

    if estimate == 'amplitude':
        np.sqrt(psds, out=psds)
        np.multiply(psds, 1e6, out=psds)
    else:
        np.multiply(psds, 1e12, out=psds)
        if '/' in unit:
            unit = '(%s)' % unit
    if dB:
        np.log10(np.maximum(psds, np.finfo(float).tiny), out=psds)
        np.multiply(psds, 10, out=psds)
    return psds

def get_peaks(all_psds, freqs):
    counts = np.bincount(np.argmax(all_psds, axis=1))
    peaks, _ = scipy.signal.find_peaks(np.concatenate(([0], counts, [0])))
    return np.take(freqs, peaks - 1)

def get_power(psds, freqs, band):
    freq_res = (freqs[-1] - freqs[0]) / len(freqs)
    idx = np.logical_and(freqs >= band.min_freq, freqs <= band.max_freq)
    psds = convert_psds(psds)
    return scipy.integrate.simps(psds[idx], dx=freq_res)

def get_unit_label(dB=False, estimate='power', unit='µV'):
    if estimate == 'auto':
        estimate = 'power' if dB else 'amplitude'

    if estimate == 'amplitude':
        label = r'$\mathrm{%s/\sqrt{Hz}}$' % unit
    else:
        if '/' in unit:
            unit = '(%s)' % unit
        label = r'$\mathrm{%s²/Hz}$' % unit
    if dB:
        label += r'$\ \mathrm{(dB)}$'
    return label