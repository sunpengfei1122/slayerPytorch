import sys, os
import numpy as np

CURRENT_TEST_DIR = os.path.dirname(os.path.realpath(__file__))
#CURRENT_TEST_DIR = '/neuromorphic/home_dirs/nicholas/slayerpytorchnc/test'
sys.path.append(CURRENT_TEST_DIR + "/../src")

from spikeFileIO import read2Dspikes, read3Dspikes, encode3Dspikes, showTD, showTDupdated

fname = "1.bs2"

exampleFile = CURRENT_TEST_DIR + "/test_files/NMNISTsmall/" + fname

TD = read2Dspikes(exampleFile)

showTDupdated(TD)

savePath = CURRENT_TEST_DIR + "/test_files/3d_test/"

encode3Dspikes(savePath+fname, TD)

TD_new = read3Dspikes(savePath+fname)

showTDupdated(TD_new)

# compares each attribute of TD
for (old_values, new_values) in zip(TD.__dict__.values(),TD_new.__dict__.values()):
    print(np.array((old_values==new_values)).all())
