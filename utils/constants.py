__all__ = ['BANDS', 'MAX_SES', 'MAX_SUB']

class Band:
    def __init__(self, min_freq, max_freq, color):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.color = color

BANDS = {
    'delta': Band(0.5, 4, 'skyblue'),
    'theta': Band(4, 7, 'hotpink'),
    'alpha': Band(8, 13, 'salmon'),
    'beta': Band(13, 30, 'lightseagreen'),
    'gamma': Band(30, 128, 'thistle')
}

MAX_SUB = 20
MAX_SES = 12
