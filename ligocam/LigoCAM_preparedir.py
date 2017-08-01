import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--cur-time", dest="curGpsTime", type="int",
                  help="Current GPS-start-time", metavar="TIME")
parser.add_option("-d", "--run-dir", dest="runDir", type="string",
                  help="Run directory", metavar="NAME")
(options, args) = parser.parse_args()

run_dir = options.runDir

ASD_dir = run_dir  + '/images/ASD/' + str(options.curGpsTime)
if not os.path.exists(ASD_dir):
    os.mkdir(ASD_dir)
TS_dir = run_dir + '/images/TS/' + str(options.curGpsTime)
if not os.path.exists(TS_dir):
    os.mkdir(TS_dir)
