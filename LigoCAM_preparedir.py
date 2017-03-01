#!/usr/bin/python

import os
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-t", "--cur-time", dest = "curGpsTime", type = "int",
                  help = "Current GPS-start-time",
                  metavar = "TIME")

(options, args) = parser.parse_args()



ASD_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/images/ASD/'+str(options.curGpsTime)
if not os.path.exists(ASD_dir):
                               os.mkdir(ASD_dir)
TS_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/images/TS/'+str(options.curGpsTime)
if not os.path.exists(TS_dir):
                              os.mkdir(TS_dir)

