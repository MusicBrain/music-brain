#!venv/bin/python

from utils import *

raw = read_raw_data(12, 1)
spectrum = raw.compute_psd()
all_psds, freqs = spectrum.get_data(return_freqs=True)

CHANNEL = 0
psds = all_psds[CHANNEL]
power = get_power(psds, freqs, BANDS['Delta'])
print(power)
