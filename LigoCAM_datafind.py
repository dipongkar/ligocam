from optparse import OptionParser
import commands
#from glue import lal
#from pylal import frutils



parser = OptionParser()


parser.add_option("-t", "--cur-time", dest = "curGpsTime", type = "int",
                  help = "Current GPS-start-time",
                  metavar = "TIME")
parser.add_option("-l", "--ifo", dest = "observatory", type="string",
                  help = "Observatory to LigoCAM",
                  metavar="NAME")
parser.add_option("-f", "--frame_type", dest = "frameType", type="string",
                  help = "Frames to LigoCAM",
                  metavar="NAME")
parser.add_option("-g", "--cache_group", dest = "Group", type="string",
                  help = "Ref or Curr cache group",
                  metavar="NAME")

(options, args) = parser.parse_args()

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

group = options.Group
cmd_temp = 'echo $TMPDIR'
temp_dir = commands.getoutput(cmd_temp)
ifo = options.observatory
observatory = ifo[0]
frame_type = ifo + '_' + options.frameType

 ## We start run at 30m past the clock for 512s data.
curgpstime = options.curGpsTime          
gpsstarttime = curgpstime - 1800
gpsendtime = gpsstarttime + 512

file_prefix = run_dir + 'cache/' + group + '_' + str(gpsstarttime) + '_'
cache_file = file_prefix + 'frame_cache.txt'
cmd_datafind = 'gw_data_find -o ' + observatory + ' -s ' + str(gpsstarttime) + ' -e ' + str(gpsendtime) + ' -t ' + frame_type + ' -u file --lal-cache > ' + cache_file
commands.getoutput(cmd_datafind)

