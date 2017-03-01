import shutil
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--cur-time", dest = "curGpsTime", type = "int",
                  help = "Current GPS-start-time",
                  metavar = "TIME")
parser.add_option("-c", "--channel-list", dest = "channelList", type = "string",
                  help = "Channels to LigoCAM",
                  metavar = "FILE")
(options, args) = parser.parse_args()

channellist = options.channelList

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

shutil.copy2(run_dir + 'alert/Disconnected_'+str(options.curGpsTime)+'_'+channellist,run_dir + 'alert/Disconnected_past_'+channellist)
shutil.copy2(run_dir + 'alert/DAQfailure_'+str(options.curGpsTime)+'_'+channellist,run_dir + 'alert/DAQfailure_past_'+channellist)  
shutil.copy2(run_dir + 'alert/Disconnmail_'+str(options.curGpsTime)+'_'+channellist,run_dir + 'alert/Disconnmail_past_'+channellist)  
shutil.copy2(run_dir + 'alert/DAQfailmail_'+str(options.curGpsTime)+'_'+channellist,run_dir + 'alert/DAQfailmail_past_'+channellist)


