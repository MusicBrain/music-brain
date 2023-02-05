#!venv/bin/python

import logging
import mne

logging.basicConfig(level='INFO', format='%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s')
logging.getLogger('mne').setLevel('ERROR')

sub_count = 1 #20
ses_count = 1 #12

sub_list = []
for sub in range(1, sub_count + 1):
    logging.info('Loading subject %03d' % sub)
    ses_list = []

    for ses in range(1, ses_count + 1):
        data_path = 'musin-g/sub-%03d/ses-%02d/eeg/sub-%03d_ses-%02d_task-MusicListening_run-%d_eeg' % (sub, ses, sub, ses, ses)
        data = mne.io.read_raw_eeglab(data_path + '.set', preload=True, montage_units='mm')
        ses_list.append(data)

    sub_list.append(ses_list)

import matplotlib.pyplot as plt
raw:mne.io.Raw = sub_list[0][0]
raw.plot(n_channels=128)
raw.plot_psd(picks=['E129'])
plt.show()
