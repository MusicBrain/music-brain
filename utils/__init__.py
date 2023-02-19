import logging
from .analysis import *
from .constants import *
from .dataset import *

logging.basicConfig(level='INFO', format='%(asctime)s %(levelname)s [%(module)s:%(lineno)d] %(message)s')
logging.getLogger('mne').setLevel('ERROR')
