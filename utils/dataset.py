__all__ = ['read_all_raw_data', 'read_raw_data']

import logging
import mne
import mne_bids
from pathlib import Path

MONTAGE = mne.channels.make_standard_montage('GSN-HydroCel-128')
ROOT = Path(__file__).parent / '..' / 'musin-g'

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
        run='1',
        root='musin-g',
        datatype='eeg')
    data = mne_bids.read_raw_bids(path, {'preload': True})
    data.set_eeg_reference(ref_channels=['E129'])
    return data
