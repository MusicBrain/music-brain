__all__ = ['BANDS', 'DEFAULT_MONTAGE', 'EASYCAP_MONTAGE', 'MAX_SES', 'MAX_SUB']

import mne

class Band:
    def __init__(self, symbol, min_freq, max_freq, color):
        self.symbol = symbol
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.color = color

BANDS = {
    'Delta': Band('$\\delta$ (delta)', 0.5, 4, 'skyblue'),
    'Theta': Band('$\\theta$ (theta)', 4, 7, 'hotpink'),
    'Alpha': Band('$\\alpha$ (alpha)', 8, 13, 'salmon'),
    'Beta': Band('$\\beta$ (beta)', 13, 30, 'lightseagreen'),
    'Gamma': Band('$\\gamma$ (gamma)', 30, 128, 'thistle')
}

MAX_SUB = 20
MAX_SES = 12

DEFAULT_MONTAGE = mne.channels.make_standard_montage('GSN-HydroCel-128')
EASYCAP_MONTAGE = mne.channels.make_standard_montage('easycap-M1')
