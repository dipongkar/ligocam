import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--cur-time", dest="curGpsTime", type="int",
                  help="Current GPS-start-time", metavar="TIME")
parser.add_option("-d", "--run-dir", dest="runDir", type="string",
                  help="Run directory", metavar="NAME")
parser.add_option("-p", "--pubhtml-dir", dest="pubhtmlDir", type="string",
                  help="PublicHTML directory", metavar="NAME")
(options, args) = parser.parse_args()

strcurGpsTime = str(options.curGpsTime)
run_dir = options.runDir
pubhtml_dir = options.pubhtmlDir

shutil.copytree(run_dir + '/images/ASD/' + strcurGpsTime, pubhtml_dir + \
                                        '/images/ASD/' + strcurGpsTime)
shutil.copytree(run_dir + '/images/TS/' + strcurGpsTime, pubhtml_dir + \
                                      '/images/TS/' + strcurGpsTime)
