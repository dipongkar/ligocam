from FindChannelAlertsLib import *
from optparse import OptionParser

# command line options
parser = OptionParser()
parser.add_option("-f", "--file", dest="dataFile",
                  help="Path to first stage LIGOCam results",
                  metavar="FILE")
parser.add_option("-d", "--dir", dest="outputDir",
                  help="Path to directory for second stage LIGOCam results",
                  metavar="DIRECTORY")
parser.add_option("-n", "--name", dest="fileName",
                  help="Name for output file (including extension)",
                  metavar="STRING")
parser.add_option("-t", "--cur-time", dest="curGpsTime", type="int",
                  help="Current GPS-start-time",
                  metavar="TIME")
(options, args) = parser.parse_args()

# read data from channel
data = read_text_file(options.dataFile + str(options.curGpsTime) + '.txt', ' ')

# find alerts
data = filter_list_of_lists(data, 12, 'Yes')

# find output directory and output file name
indeces = find_char_indeces('/', options.dataFile)
# find output file name
if options.fileName:
    outputName = options.fileName + str(options.curGpsTime) + '.txt'
else:
    # find input file name
    if indeces:
        inputName = options.dataFile[indeces[-1]+1:]
    else:
        inputName = options.dataFile
    defaultAddOn = "Stage2"
    indeces2 = find_char_indeces('.', inputName)
    outputName = inputName[:indeces2[-1]] + defaultAddOn + \
                                    inputName[indeces2[-1]:]
    # find output directory
if options.outputDir:
    outDir = options.outputDir
else:
    # find input directory
    if indeces:
        inDir = options.dataFile[:indeces[-1]]
    else:
        inDir = ""
    outDir = inDir
    # find full output file path
if outDir:
    outPath = outDir + '/' + outputName
else:
    outPath = outputName
#print(outPath)

# print data to new file
print_filtered_data_to_file(data, outPath)
