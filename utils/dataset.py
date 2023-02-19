__all__ = ['read_all_raw_data', 'read_raw_data']

import logging
import mne
from pathlib import Path

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
    data_path = ROOT / ('sub-%03d' % sub) / ('ses-%02d' % ses) / 'eeg' / ('sub-%03d_ses-%02d_task-MusicListening_run-%d_eeg.set' % (sub, ses, ses))
    data = mne.io.read_raw_eeglab(data_path, preload=True, montage_units='mm')
    data.drop_channels(['E129'])
    return data
