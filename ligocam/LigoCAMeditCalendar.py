import sys
import os
import shutil
import fileinput
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--cur-time", dest="curGpsTime", type="int",
                  help="Current GPS-start-time", metavar="TIME")
parser.add_option("-a", "--ymdh-string", dest="ymdhstring", type="string",
                  help="Current ymdh", metavar="TIME")
parser.add_option("-u", "--hour-string", dest="hourstring", type="string",
                  help="Current hour", metavar="TIME")
parser.add_option("-m", "--month-string", dest="monthstring", type="string",
                  help="Current month", metavar="TIME")
parser.add_option("-y", "--year-string", dest="yearstring", type="string",
                  help="Current year", metavar="TIME")
parser.add_option("-p", "--pubhtml-dir", dest="pubhtmlDir", type="string",
                  help="PublicHTML directory", metavar="NAME")
parser.add_option("-U", "--pub-url", dest="pubUrl", type="string",
                  help="Public URL", metavar="NAME")
(options, args) = parser.parse_args()

pubhtml_dir = options.pubhtmlDir
strcurGpsTime = str(options.curGpsTime)
ymdhstring = options.ymdhstring
hourstring = options.hourstring
monthstring = options.monthstring
yearstring = options.yearstring
puburl = options.pubUrl

stringold = '<!-- ' + ymdhstring + ' --> <li class="sgrayl l1"><p>' + \
                                                 hourstring + ':00</p></li>'
stringnew = '<li class="greenish l1"><p><a href="' + puburl + \
           '/pages/LigoCamHTML_' + strcurGpsTime + '.html">' + \
                               hourstring + ':00</a></p></li>'
html_file = pubhtml_dir + '/calendar/LigoCAM_' + monthstring + '_' + \
                                                 yearstring + '.html'
html_file_temp = pubhtml_dir + '/calendar/LigoCAM_' + monthstring + '_' + \
                                yearstring + '_' + strcurGpsTime + '.html'
shutil.copy2(html_file, html_file_temp)
html_page = pubhtml_dir + '/pages/LigoCamHTML_' + strcurGpsTime + '.html'
pagestat = os.stat(html_page)
page_size = pagestat.st_size
if page_size > 2000:
    for j, line in enumerate(fileinput.input(html_file_temp, inplace=1)):
        sys.stdout.write(line.replace(stringold, stringnew))
else:
    print "html tables empty"
filestat = os.stat(html_file_temp)
file_size = filestat.st_size
if file_size > 10:
    shutil.copy2(html_file_temp, html_file)
else:
    print "error occurred"
os.remove(html_file_temp)
