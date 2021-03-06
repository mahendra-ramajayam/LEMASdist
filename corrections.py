"""
Correction values for each sensor
If these ever need changed, the format is: corrections['<serial number>'] = [<temperature correction, deg. C>, <humidity correction, %RH>]
Add new sensors below the last line
"""
corrections = {}                                                                 #initialize empty dictionary

corrections[''] = [0, 0]                                                         #default corrections when no sensor ID exists
corrections['17968243'] = [-0.02, -1.5]
corrections['18960415'] = [-0.05, 0.02]
corrections['18960416'] = [-0.02, -0.02]
corrections['18960417'] = [-0.05, -0.02]
corrections['18960418'] = [-0.02, -0.31]
corrections['18960419'] = [0.00, -0.48]
corrections['18960420'] = [-0.04, -0.04]
corrections['18960421'] = [0.04, 0.31]
corrections['18960422'] = [-0.04, -0.03]
corrections['18960423'] = [0.05, -0.89]
corrections['18960424'] = [-0.10, 0.11]
corrections['18960425'] = [0.01, 0.04]
corrections['18960426'] = [-0.05, 0.36]
corrections['18960427'] = [-0.01, 0.16]
corrections['18960429'] = [0.00, 0.06]
corrections['18960430'] = [-0.11, 0.08]
corrections['18960431'] = [0.03, 0.02]
corrections['18960432'] = [-0.07, 0.19]
corrections['18960433'] = [0.01, 0.26]
corrections['18960434'] = [-0.11, -0.30]
corrections['18960435'] = [-0.08, -0.21]
corrections['18960436'] = [0.04, -0.37]
corrections['18960437'] = [-0.09, -0.27]
corrections['18960438'] = [-0.04, 0.00]
corrections['18960439'] = [-0.04, -0.04]
corrections['18960442'] = [-0.12, -0.14]
corrections['18960443'] = [-0.02, 0.17]
corrections['18960444'] = [0.10, 0.08]
#corrections['sensor serial number'] = [<temperature correction>, <humidity correction>]
