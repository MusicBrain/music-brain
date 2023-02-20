#!venv/bin/python

import mne_bids
from utils import *

path = mne_bids.BIDSPath(
    subject='001',
    session='01',
    task='MusicListening',
    run='1',
    root='musin-g',
    datatype='eeg')
raw = mne_bids.read_raw_bids(path, {'preload': True})
print(raw.describe())
