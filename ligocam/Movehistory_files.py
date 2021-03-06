import shutil
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--run-dir", dest="runDir", type="string",
                  help="Run directory", metavar="NAME")
(options, args) = parser.parse_args()

run_dir = options.runDir
Disconn_now = run_dir + '/results/Disconnected_now.txt'
DAQfail_now = run_dir + '/results/DAQfailure_now.txt'

disfilestat = os.stat(Disconn_now)
disfile_size = disfilestat.st_size
if disfile_size > 2:
    shutil.copy2(run_dir + '/results/Disconnected_now.txt', run_dir + \
                                    '/results/Disconnected_past.txt')
else:
    print "current file is empty"

daqfilestat = os.stat(DAQfail_now)
daqfile_size = daqfilestat.st_size
if daqfile_size > 2:
    shutil.copy2(run_dir + '/results/DAQfailure_now.txt', run_dir + \
                                    '/results/DAQfailure_past.txt')
else:
    print "current file is empty"
