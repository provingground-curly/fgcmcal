"""
HSC cookbook specific overrides for fgcmOutputProducts
"""

import os.path

from lsst.utils import getPackageDir

# Last cycle number that was run, preferably with outputStandards == True
config.cycleNumber = 3

# Reference object info
config.refObjLoader.ref_dataset_name = 'ps1_pv3_3pi_20170110'

# Photometric calibration information
config.photoCal.photoCatName = 'ps1'
hscConfigDir = os.path.join(getPackageDir("obs_subaru"), "config", "hsc")
config.photoCal.colorterms.load(os.path.join(hscConfigDir, 'colorterms.py'))



