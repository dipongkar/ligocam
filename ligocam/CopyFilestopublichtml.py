import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--cur-time", dest="curGpsTime", type="int",
                  help="Current GPS-start-time", metavar="TIME")
(options, args) = parser.parse_args()

strcurGpsTime = str(options.curGpsTime)

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'
pub_dir = '/home/dtalukder/public_html/Projects/detchar/LigoCAM/PEM/'

shutil.copytree(run_dir + 'images/ASD/' + strcurGpsTime, pub_dir + \
                                        'images/ASD/' + strcurGpsTime)
shutil.copytree(run_dir + 'images/TS/' + strcurGpsTime, pub_dir + \
                                      'images/TS/' + strcurGpsTime)
