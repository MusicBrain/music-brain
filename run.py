#!venv/bin/python

import matplotlib.pyplot as plt
import numpy as np
from utils import *

CHANNEL = 79

raw = read_raw_data(1, 1)
spectrum = raw.compute_psd()
all_psds, freqs = spectrum.get_data(return_freqs=True)

plt.figure(figsize=(12, 4))

psds = all_psds[CHANNEL]
psds_db = convert_psds(psds, dB=True)

plt.xlabel('Frequency (Hz)')
plt.ylabel(get_unit_label(dB=True))
plt.plot(freqs, psds_db, lw=1, color='black')

for name in BANDS.keys():
    band = BANDS[name]
    idx = np.logical_and(freqs >= band.min_freq, freqs <= band.max_freq)
    plt.fill_between(freqs, psds_db, y2=psds_db.min(), where=idx, color=band.color)

plt.tick_params(length=3)
plt.xticks(
    [np.average([band.min_freq, band.max_freq]) for band in BANDS.values()],
    BANDS.keys(),
    rotation=-60,
    rotation_mode='anchor',
    ha='left'
)

text = ''
for name in BANDS.keys():
    band = BANDS[name]
    power = get_power(psds, freqs, BANDS[name])
    unit = get_unit_label()
    text += '%s (%.1f-%.1f Hz):\t%.3f %s\n' % (name, band.min_freq, band.max_freq, power, unit)
plt.text(len(psds_db), psds_db.max(), text, ha='right', va='top')

peaks = get_peaks(all_psds, freqs)
for peak in peaks:
    plt.vlines(peak, psds_db.min(), psds_db.max(), color='darkblue', lw=0.5, linestyles='dashed')

plt.show()
plt.close()
