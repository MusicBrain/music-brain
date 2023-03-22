#!venv/bin/python

import matplotlib.pyplot as plt
import numpy as np
import scipy
from utils import *

CHANNEL = 79

raw = read_raw_data(1, 1)
spectrum = raw.compute_psd()
all_psds, freqs = spectrum.get_data(return_freqs=True)

fig, ax = plt.subplots(figsize=(12, 4))

psds = all_psds[CHANNEL]
psds_db = convert_psds(psds, dB=True)
interp_psds, interp_freqs = insert_band_boundaries(psds, freqs)
interp_psds_db = convert_psds(interp_psds, dB=True)

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel(get_unit_label(dB=True))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.plot(interp_freqs, interp_psds_db, lw=1, color='black')

for name in BANDS.keys():
    band = BANDS[name]
    idx = np.logical_and(interp_freqs >= band.min_freq, interp_freqs <= band.max_freq)
    plt.fill_between(interp_freqs, interp_psds_db, y2=interp_psds_db.min(), where=idx, color=band.color)

ax.tick_params(length=3)

cell_text = []
cell_colors = []
for name in BANDS.keys():
    band = BANDS[name]
    power = get_power(psds, freqs, BANDS[name])
    unit = get_unit_label()
    cell_text.append([band.symbol, '%.1f-%.1f Hz' % (band.min_freq, band.max_freq), '%.3f %s' % (power, unit)])
    cell_colors.append([band.color, band.color, band.color])
tab = ax.table(cell_text, cellColours=cell_colors, cellLoc='left', colLabels=['Band', 'Range', 'Avg Power'], loc='upper right')
tab.auto_set_column_width([0, 1, 2])
tab.auto_set_font_size(False)
tab.set_fontsize(9)

peaks, _ = scipy.signal.find_peaks(psds_db, prominence=1)
for peak in peaks:
    ax.vlines(freqs[peak], psds_db.min(), psds_db[peak], color='darkblue', lw=0.5, linestyles='dashed')
    ax.text(freqs[peak], psds_db[peak], '%0.3f' % psds_db[peak], fontsize=9, ha='center', va='bottom')
ax.set_xticks(np.take(freqs, peaks))

plt.show()
plt.close()
