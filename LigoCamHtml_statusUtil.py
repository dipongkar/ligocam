#from html import HTML
import LigoCamHtmlLib as CamHtml
#import numpy as np
#import asciitable
#from optparse import OptionParser
#import os, commands
#import shutil
#import subprocess

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'
pubhtml_dir = '/home/dtalukder/public_html/Projects/detchar/LigoCAM/PEM/'

def ligocam_makehtml_status(line,strcurUtcTime,curGpsTime):

  t = CamHtml.Table(header_row=[CamHtml.TableCell('Channel name',width='31%',header=True), CamHtml.TableCell('STATUS',width='7%',header=True), CamHtml.TableCell('Disconnected?',width='6%',header=True), CamHtml.TableCell('DAQ<BR>failure?',width='4%',header=True), CamHtml.TableCell('BLRMS<BR>change',width='4%',header=True), CamHtml.TableCell('0.03-0.1',width='4%',header=True), CamHtml.TableCell('0.1-0.3',width='4%',header=True), CamHtml.TableCell('0.3-1',width='4%',header=True),CamHtml.TableCell ('1-3',width='4%',header=True), CamHtml.TableCell('3-10',width='4%',header=True), CamHtml.TableCell('10-30',width='4%',header=True), CamHtml.TableCell('30-100',width='4%',header=True), CamHtml.TableCell('100-<BR>300',width='4%',header=True), CamHtml.TableCell('300-<BR>1000',width='4%',header=True), CamHtml.TableCell('1000-<BR>3000',width='4%',header=True), CamHtml.TableCell('3000-<BR>10000',width='4%',header=True), CamHtml.TableCell('Image',width='4%',header=True)])

  thd1g = 1000; thd1l = 0.002
  thd2g = 50; thd2l = 0.2


  word = line.split()
  chan = word[0]
  band1 = word[1]
  band2 = word[2]
  band3 = word[3]
  band4 = word[4]
  band5 = word[5]
  band6 = word[6]
  band7 = word[7]
  band8 = word[8]
  band9 = word[9]
  band10 = word[10]
  band11 = word[11]
  excess = word[12]
  comb = word[13]
  disconnect = word[14]
  status = word[15]
  disconhour = word[16]
  daqfailhour = word[17]
  chan_rn = chan.replace(':', '_')
  chan_replace = chan.replace(':','%3A')
  chan_rstrip = chan_replace.rstrip('_DQ')
  if float(band1) > thd1g or float(band1) < thd1l and float(band1) !=0:
       if '_ACC_' in chan or '_MIC_' in chan:
           band1 = CamHtml.TableCell(band1,bgcolor='E8E8E8',width='4%')
       else:
           band1 = CamHtml.TableCell(band1,bgcolor='FFD280',width='4%')
  elif float(band1) == 0:
       band1 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band1 = CamHtml.TableCell(band1,bgcolor='white',width='4%')
  if float(band2) > thd1g or float(band2) < thd1l and float(band2) !=0:
       if '_ACC_' in chan or '_MIC_' in chan:
           band2 = CamHtml.TableCell(band2,bgcolor='E8E8E8',width='4%')
       else:
           band2 = CamHtml.TableCell(band2,bgcolor='FFD280',width='4%')
  elif float(band2) == 0:
       band2 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band2 = CamHtml.TableCell(band2,bgcolor='white',width='4%')
  if float(band3) > thd1g or float(band3) < thd1l and float(band3) !=0:
       if '_ACC_' in chan or '_MIC_' in chan:
           band3 = CamHtml.TableCell(band3,bgcolor='E8E8E8',width='4%')
       else:
           band3 = CamHtml.TableCell(band3,bgcolor='FFD280',width='4%')
  elif float(band3) == 0:
       band3 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band3 = CamHtml.TableCell(band3,bgcolor='white',width='4%')
  if float(band4) > thd2g or float(band4) < thd2l and float(band4) !=0:
       if '_ACC_' in chan or '_MIC_' in chan:
           band4 = CamHtml.TableCell(band4,bgcolor='E8E8E8',width='4%')
       else:
           band4 = CamHtml.TableCell(band4,bgcolor='FFD280',width='4%')
  elif float(band4) == 0:
       band4 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band4 = CamHtml.TableCell(band4,bgcolor='white',width='4%')
  if float(band5) > thd2g or float(band5) < thd2l and float(band5) !=0:
       if '_ACC_' in chan or '_MIC_' in chan:
           band5 = CamHtml.TableCell(band5,bgcolor='E8E8E8',width='4%')
       else:
           band5 = CamHtml.TableCell(band5,bgcolor='FFD280',width='4%')
  elif float(band5) == 0:
       band5 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band5 = CamHtml.TableCell(band5,bgcolor='white',width='4%')
  if float(band6) > thd2g or float(band6) < thd2l and float(band6) !=0:
       band6 = CamHtml.TableCell(band6,bgcolor='FFD280',width='4%')
  elif float(band6) == 0:
       band6 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band6 = CamHtml.TableCell(band6,bgcolor='white',width='4%')
  if float(band7) > thd2g or float(band7) < thd2l and float(band7) !=0:
       if '_SEIS_' in chan:
           band7 = CamHtml.TableCell(band7,bgcolor='E8E8E8',width='4%')
       else: 
           band7 = CamHtml.TableCell(band7,bgcolor='FFD280',width='4%')
  elif float(band7) == 0:
       band7 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band7 = CamHtml.TableCell(band7,bgcolor='white',width='4%')
  if float(band8) > thd2g or float(band8) < thd2l and float(band8) !=0:
       if '_SEIS_' in chan:
           band8 = CamHtml.TableCell(band8,bgcolor='E8E8E8',width='4%')
       else:
           band8 = CamHtml.TableCell(band8,bgcolor='FFD280',width='4%') 
  elif float(band8) == 0:
       band8 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band8 = CamHtml.TableCell(band8,bgcolor='white',width='4%')
  if float(band9) > thd2g or float(band9) < thd2l and float(band9) !=0:
       if '_SEIS_' in chan:
           band9 = CamHtml.TableCell(band9,bgcolor='E8E8E8',width='4%')
       else:
           band9 = CamHtml.TableCell(band9,bgcolor='FFD280',width='4%')
  elif float(band9) == 0:
       band9 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band9 = CamHtml.TableCell(band9,bgcolor='white',width='4%')
  if float(band10) > thd2g or float(band10) < thd2l and float(band10) !=0:
       if '_SEIS_' in chan:
           band10 = CamHtml.TableCell(band10,bgcolor='E8E8E8',width='4%')
       else:
           band10 = CamHtml.TableCell(band10,bgcolor='FFD280',width='4%')
  elif float(band10) == 0:
       band10 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band10 = CamHtml.TableCell(band10,bgcolor='white',width='4%')
  if float(band11) > thd2g or float(band11) < thd2l and float(band11) !=0:
       if '_SEIS_' in chan:
           band11 = CamHtml.TableCell(band11,bgcolor='E8E8E8',width='4%')
       else:
           band11 = CamHtml.TableCell(band11,bgcolor='FFD280',width='4%')
  elif float(band11) == 0:
       band11 = CamHtml.TableCell(' ',bgcolor='white',width='4%')
  else:
       band11 = CamHtml.TableCell(band11,bgcolor='white',width='4%')
  if excess == 'Yes':
       excess = CamHtml.TableCell(excess,bgcolor='FFD280',width='4%')
  else:
       excess = CamHtml.TableCell(excess,bgcolor='white',width='4%')
  if comb == 'Yes':
       comb = CamHtml.TableCell(comb+'     ('+daqfailhour+' h)',bgcolor='FF9771',width='4%')
  else:
       comb = CamHtml.TableCell(comb,bgcolor='white',width='4%')
  if disconnect == 'Yes':
       disconnect = CamHtml.TableCell(disconnect+'     ('+disconhour+' h)',bgcolor='FF6633',width='6%')
  else:
       disconnect = CamHtml.TableCell(disconnect,bgcolor='white',width='6%')
  if status == 'Alert':
       status = CamHtml.TableCell('ALERT',bgcolor='FFFF00',width='7%')
  else:
       status = CamHtml.TableCell('OK',bgcolor='00FF00',width='7%')
  image = ('<a href="https://ldas-jobs.ligo-wa.caltech.edu/~dtalukder/Projects/detchar/LigoCAM/PEM/images/ASD/%s/%s" target="_blank">ASD</a>, <a href="https://ldas-jobs.ligo-wa.caltech.edu/~dtalukder/Projects/detchar/LigoCAM/PEM/images/TS/%s/%s" target="_blank">TS</a>' %(curGpsTime,chan_rn+'.png',curGpsTime,chan_rn+'.png'))
  image = CamHtml.TableCell(image,bgcolor='white',width='4%')
  chan = CamHtml.TableCell(chan,bgcolor='white',width='31%')
  t.rows.append([chan, status, disconnect, comb, excess, band1, band2, band3, band4, band5, band6, band7, band8, band9, band10, band11, image])

# open an HTML file to show output in a browser
  HTMLFILE = pubhtml_dir + 'status/'+chan_rn+'_status.html'
  f = open(HTMLFILE, 'w')

  htmlcode = str(t)
  print htmlcode
  f.write('<!DOCTYPE html>\n')
  f.write('<html lang="en" class="no-js">\n\n')
  f.write('         <head>\n')
  f.write('                <meta charset="UTF-8" />\n')
  f.write('		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n')
  f.write('		<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
  f.write('		<title>LigoCAM @ LHO | PEM</title>\n')
  f.write('		<link rel="stylesheet" type="text/css" href="css/component.css" />\n')
  f.write('	  </head>\n\n')
  f.write('	  <body>\n')
  f.write('		<div class="header" style="color:green; background-color:#C8C8C8;">\n')
  f.write('                  <h1>LigoCAM</h1>\n')
  f.write('	        </div>\n')
  f.write('<p align="center" style="background-color:white;color:black;font-size:20px;margin-top:1px;margin-bottom:1px;">\n')
  f.write('Epoch: %s </p>\n' %strcurUtcTime)
  f.write('                      <table class="">\n')
  f.write('<thead>\n')
  f.write(htmlcode)
  f.write('\n 	        	</table>\n\n')
  f.write('      <script src="js/jquery.min.js"></script>\n')
  f.write('      <script src="js/jquery.ba-throttle-debounce.min.js"></script>\n')
  f.write('      <script src="js/jquery.stickyheader.js"></script>\n\n')
  f.write('         </body>\n')
  f.write('</html>')
  print '-'*79

  f.close()


def ligocam_makehtml_status_nodata(chan,curGpsTime):
  chan = chan.rstrip()
  chan_rn = chan.replace(':', '_')
  resultfile = run_dir + 'results/Result_sorted_2_'+str(curGpsTime)+'.txt'
  #resultfile = run_dir + 'results/Result_sorted'+str(curGpsTime)+'.txt'
  if chan not in open(resultfile).read():
     status_err = open(pubhtml_dir + 'status/'+chan_rn+'_status.html','w')
     status_err.write('No data or not enough data to determine the status.')
     status_err.close()
 
