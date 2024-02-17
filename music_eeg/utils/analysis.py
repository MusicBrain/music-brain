__all__ = ['convert_psds', 'get_power', 'get_unit_label', 'insert_band_boundaries']

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

def get_peaks0(all_psds):
    counts = np.bincount(np.argmax(all_psds, axis=1))
    peaks, _ = scipy.signal.find_peaks(np.concatenate(([0], counts, [0])))
    return peaks - 1

def get_power(psds, freqs, band):
    idx = np.logical_and(freqs > band.min_freq, freqs < band.max_freq)
    y = psds[idx]
    x = freqs[idx]

    left = np.interp(band.min_freq, freqs, psds)
    y = np.insert(y, 0, left)
    x = np.insert(x, 0, band.min_freq)

    right = np.interp(band.max_freq, freqs, psds)
    y = np.append(y, right)
    x = np.append(x, band.max_freq)

    power = np.array([scipy.integrate.simps(y, x)])
    power = convert_psds(power, dB=True)
    return power[0]

def get_power0(psds, freqs, band):
    freq_res = (freqs[-1] - freqs[0]) / len(freqs)
    idx = np.logical_and(freqs >= band.min_freq, freqs <= band.max_freq)
    y = convert_psds(psds[idx])
    return scipy.integrate.simps(y, dx=freq_res)

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

def insert_band_boundaries(psds, freqs):
    for band in BANDS.values():
        for freq in [band.min_freq, band.max_freq]:
            idx = freqs.searchsorted(freq, 'right') - 1
            if idx < 0:
                psds = np.insert(psds, 0, np.interp(freq, freqs, psds))
                freqs = np.insert(freqs, 0, freq)
            elif freqs[idx] < freq:
                psds = np.insert(psds, idx + 1, np.interp(freq, freqs, psds))
                freqs = np.insert(freqs, idx + 1, freq)
    return (psds, freqs)
