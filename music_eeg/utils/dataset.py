__all__ = ['read_all_raw_data', 'read_raw_data']

import logging
import mne_bids
from .constants import *

def read_all_raw_data(max_sub, max_ses):
    sub_list = []
    for sub in range(1, max_sub + 1):
        logging.info('Loading subject %03d' % sub)
        ses_list = []

        for ses in range(1, max_ses + 1):
            ses_list.append(read_raw_data(sub, ses))

        sub_list.append(ses_list)
    return sub_list

def read_raw_data(sub, ses):
    path = mne_bids.BIDSPath(
        subject='%03d' % sub,
        session='%02d' % ses,
        task='MusicListening',
        run='%d' % ses,
        root='musin-g',
        datatype='eeg')
    data = mne_bids.read_raw_bids(path, {'preload': True})
    data.drop_channels(['E129'])
    data.set_montage(DEFAULT_MONTAGE)
    return data
