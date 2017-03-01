from __future__ import division
#from numpy import *
import numpy as np
#from pylab import *
#import matplotlib.pyplot as plt
#from matplotlib.mlab import *
#from scipy import stats
#import os
#import nds2
#from optparse import OptionParser
import LigoCAM_plotutils as pltutils
#import shutil

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

comb_th = 1e-8
comb_seis_th = 1e-7
comb_lowfmictemperature_th = 0.5e-3
comb_tilt_th = 0.5e-3
comb_0p3to20hz_th = 1e-6
comb_1to40hz_th = 1e-7
disconnect_4097_case_th = 0.44
disconnect_8193_case_th = 0.62
disconnect_16385_case_th = 0.88
disconnect_32769_case_th = 1.25
disconnect_65537_case_th = 1.78
#disconnect_th = 0.2
disconnect_seis_th = 0.1
#disconnect_accmic_th = 0.33
disconnect_th = 2.0
#disconnect_seis_th = 1.0
#disconnect_accmic_th = 3.4
#disconnect_accmic_th = 1.7
disconnect_accmic_th = 1.2
disconnect_lowfmictemperature_th = 0.1
disconnect_tilt_th = 0.2
disconnect_magmainsmon_th = 0.2
disconnect_128hzmainsmon_th = 0.18
magasdat60hz = 1000
#magasdat60hz = 200
magexcasdat60hz = 100
mainsmonat60hz = 1000
thd1g = 1000; thd1l = 1/500
thd2g = 50; thd2l = 1/5

alpha = 2/(1+12)

rng1 = range(16,52)
rng2 = range(52,154)
rng3 = range(154,512)
rng4 = range(512,1536)
rng5 = range(1536,5120)
rng6 = range(5120,15360)
rng7 = range(15360,51200)
rng8 = range(51200,153600)
rng9 = range(153600,512000)
rng10 = range(512000,1536000)


def get_disconnected_yes_hour(x_n):
  ff = open(run_dir + 'results/Disconnected_past.txt','r')
  hournew = 0
  for line in ff.readlines():
     word = line.split()
     chan = word[0]
     hour = word[1]
     if chan == x_n:
          hournew = hournew + float(hour) + 1 
          break         
     else:
          notinterested = 'ignore'
  ff.close()
  if hournew == 0:
     hournew = 1
  else:
     hournew = hournew
  return hournew

def get_daqfailure_yes_hour(x_n):
  ff = open(run_dir + 'results/DAQfailure_past.txt','r')
  hournew = 0
  for line in ff.readlines():
     word = line.split()
     chan = word[0]
     hour = word[1]
     if chan == x_n:
          hournew = hournew + float(hour) + 1 
          break         
     else:
          notinterested = 'ignore'
  ff.close()
  if hournew == 0:
     hournew = 1
  else:
     hournew = hournew
  return hournew



def do_all_for_4097_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng5n = range(1536,4096)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5n]; p_5 = Pxx[rng5n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:303]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)
                      
        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        rng0p3_5 = range(154,5*512)
        p0p3_5 = Pxx[rng0p3_5]
        if np.sqrt(sum(p0p3_5)*1/512) < disconnect_4097_case_th and np.amin(np.sqrt(p0p3_5)) > comb_0p3to20hz_th:
                   disconnect = 'Yes'
        else:      disconnect = 'No'

        if np.amin(np.sqrt(p0p3_5)) < comb_0p3to20hz_th:
                   comb = 'Yes'
        else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0


        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = 0
	pc_7 = 0
	pc_8 = 0
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_4097_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,p_1,p_2,p_3,p_4,p_5,fb_3,fb_4,fb_5,pb_3,pb_4,pb_5,pr_1,pr_2,prb_3,prb_4,prb_5)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_8193_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng6n = range(5120,8192)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6n]; p_6 = Pxx[rng6n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:344]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        rng0p3_10 = range(154,10*512)
        p0p3_10 = Pxx[rng0p3_10]
        if np.sqrt(sum(p0p3_10)*1/512) < disconnect_8193_case_th and np.amin(np.sqrt(p0p3_10)) > comb_0p3to20hz_th:
                   disconnect = 'Yes'
        else:      disconnect = 'No'

        if np.amin(np.sqrt(p0p3_10)) < comb_0p3to20hz_th:
                   comb = 'Yes'
        else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0


        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = 0
	pc_8 = 0
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_8193_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,p_1,p_2,p_3,p_4,p_5,p_6,fb_3,fb_4,fb_5,fb_6,pb_3,pb_4,pb_5,pb_6,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_16385_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng7n = range(15360,16384)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7n]; p_7 = Pxx[rng7n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:418]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        rng1_20 = range(512,20*512)
        p1_20 = Pxx[rng1_20]
        if np.sqrt(sum(p1_20)*1/512) < disconnect_16385_case_th and np.amin(np.sqrt(p1_20)) > comb_0p3to20hz_th:
                   disconnect = 'Yes'
        else:      disconnect = 'No'

        if np.amin(np.sqrt(p1_20)) < comb_0p3to20hz_th:
                   comb = 'Yes'
        else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0


        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = 0
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)  
        pltutils.psdplot_16385_and_32769_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,p_1,p_2,p_3,p_4,p_5,p_6,p_7,fb_3,fb_4,fb_5,fb_6,fb_7,pb_3,pb_4,pb_5,pb_6,pb_7,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_32769_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng7n = range(15360,32768)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7n]; p_7 = Pxx[rng7n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:434]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        rng1_40 =range(512,40*512)
        p1_40 = Pxx[rng1_40]
        if np.sqrt(sum(p1_40)*1/512) < disconnect_32769_case_th and np.amin(np.sqrt(p1_40)) > comb_1to40hz_th:
                   disconnect = 'Yes'
        else:      disconnect = 'No'
        
        if np.amin(np.sqrt(p1_40)) < comb_1to40hz_th:
                   comb = 'Yes'
        else:      comb = 'No'
        
        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else: 
            disconhour = 0
        
        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0


        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = 0
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)  
        pltutils.psdplot_16385_and_32769_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,p_1,p_2,p_3,p_4,p_5,p_6,p_7,fb_3,fb_4,fb_5,fb_6,fb_7,pb_3,pb_4,pb_5,pb_6,pb_7,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_65537_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng8n = range(51200,65536)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8n]; p_8 = Pxx[rng8n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:467]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_LOWFMIC_' in x_n or '_TEMPERATURE_' in x_n:
            rng_lowfmictemp = range(16,154)
            p_lowfmictemp = Pxx[rng_lowfmictemp]
            if np.sqrt(sum(p_lowfmictemp)*1/512) < disconnect_lowfmictemperature_th and np.amin(np.sqrt(p_lowfmictemp)) > comb_lowfmictemperature_th*0.1:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            comb_amp = np.sqrt(p_lowfmictemp)
            comb_num = sum(j < comb_lowfmictemperature_th for j in comb_amp)
            if comb_num > 5:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_TILT_' in x_n:
            rng_tilt = range(16,512)
            p_tilt = Pxx[rng_tilt]
            if np.sqrt(sum(p_tilt)*1/512) < disconnect_tilt_th and np.amin(np.sqrt(p_tilt)) > comb_tilt_th*0.1:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            comb_amp = np.sqrt(p_tilt)
            comb_num = sum(j < comb_tilt_th for j in comb_amp)
            if comb_num > 5:
                       comb = 'Yes'
            else:      comb = 'No'

# Special case for 256hz incorrect LHO MAINSMON
        elif '_MAINSMON_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_80 = range(61*512,80*512+1)
            rng10_80 = rng10_59 + rng61_80
            p10_80 = Pxx[rng10_80]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
            if np.sqrt(sum(p10_80)*1/512) < disconnect_128hzmainsmon_th and np.amin(np.sqrt(p10_80)) > comb_th and np.amax(p59_61) < mainsmonat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_80)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng1_59 = range(512,59*512+1)
            rng61_80 = range(61*512,80*512+1)
            rng1_80 = rng1_59 + rng61_80
            p1_80 = Pxx[rng1_80]
            if np.sqrt(sum(p1_80)*1/512) < disconnect_65537_case_th and np.amin(np.sqrt(p1_80)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p1_80)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_65537_and_131073_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'
 
        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_131073_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng8n = range(51200,131072)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8n]; p_8 = Pxx[rng8n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:532]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = 0
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)  
        pltutils.psdplot_65537_and_131073_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_262145_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng9n = range(153600,262144)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9n]; p_9 = Pxx[rng9n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:566]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)
 
        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

# Mar 31, 2015 LHO made this choice. 
        elif '_MAINSMON_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < mainsmonat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = 0
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)  
        pltutils.psdplot_262145_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_524289_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng10n = range(512000,524288)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9]; p_9 = Pxx[rng9]
        f_10 = freq[rng10n]; p_10 = Pxx[rng10n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]; prb_10 = Pxx_r[591:593]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        chunksize = 10000
        numchunks = p_10.size // chunksize 
        p_10chunks = p_10[:chunksize*numchunks].reshape((-1, chunksize))
        f_10chunks = f_10[:chunksize*numchunks].reshape((-1, chunksize))
        pb_10 = p_10chunks.mean(axis=1)
        fb_10 = f_10chunks.mean(axis=1)
        if len(p_10) > chunksize*numchunks:
           p_10_edge = p_10[range(chunksize*numchunks,len(p_10))]
           pb_10_edge = np.array([p_10_edge.mean()])  
           pb_10 = np.concatenate((pb_10,pb_10_edge), axis=0)
           f_10_edge = f_10[range(chunksize*numchunks,len(f_10))]
           fb_10_edge = np.array([f_10_edge.mean()])  
           fb_10 = np.concatenate((fb_10,fb_10_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

# Suppose to be this one
        elif '_MAINSMON_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < mainsmonat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = np.sqrt(sum(pb_10))/np.sqrt(sum(prb_10))
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)  
        pltutils.psdplot_524289_and_1048577_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,fb_10,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_1048577_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng10n = range(512000,1048576)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9]; p_9 = Pxx[rng9]
        f_10 = freq[rng10n]; p_10 = Pxx[rng10n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]; prb_10 = Pxx_r[591:645]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        chunksize = 10000
        numchunks = p_10.size // chunksize 
        p_10chunks = p_10[:chunksize*numchunks].reshape((-1, chunksize))
        f_10chunks = f_10[:chunksize*numchunks].reshape((-1, chunksize))
        pb_10 = p_10chunks.mean(axis=1)
        fb_10 = f_10chunks.mean(axis=1)
        if len(p_10) > chunksize*numchunks:
           p_10_edge = p_10[range(chunksize*numchunks,len(p_10))]
           pb_10_edge = np.array([p_10_edge.mean()])  
           pb_10 = np.concatenate((pb_10,pb_10_edge), axis=0)
           f_10_edge = f_10[range(chunksize*numchunks,len(f_10))]
           fb_10_edge = np.array([f_10_edge.mean()])  
           fb_10 = np.concatenate((fb_10,fb_10_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-CS_MAG_LVEA_INPUTOPTICS_Y_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-EX_MAG_VEA_FLOOR_X_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-EX_MAG_VEA_FLOOR_Y_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_MAG_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = np.sqrt(sum(pb_10))/np.sqrt(sum(prb_10))
	pc_11 = 0

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_524289_and_1048577_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,fb_10,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_2097153_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng11n = range(1536000,2097152)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9]; p_9 = Pxx[rng9]
        f_10 = freq[rng10]; p_10 = Pxx[rng10]
        f_11 = freq[rng11n]; p_11 = Pxx[rng11n]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]; prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:700]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        chunksize = 10000
        numchunks = p_10.size // chunksize 
        p_10chunks = p_10[:chunksize*numchunks].reshape((-1, chunksize))
        f_10chunks = f_10[:chunksize*numchunks].reshape((-1, chunksize))
        pb_10 = p_10chunks.mean(axis=1)
        fb_10 = f_10chunks.mean(axis=1)
        if len(p_10) > chunksize*numchunks:
           p_10_edge = p_10[range(chunksize*numchunks,len(p_10))]
           pb_10_edge = np.array([p_10_edge.mean()])  
           pb_10 = np.concatenate((pb_10,pb_10_edge), axis=0)
           f_10_edge = f_10[range(chunksize*numchunks,len(f_10))]
           fb_10_edge = np.array([f_10_edge.mean()])  
           fb_10 = np.concatenate((fb_10,fb_10_edge), axis=0)

        chunksize = 100000
        numchunks = p_11.size // chunksize 
        p_11chunks = p_11[:chunksize*numchunks].reshape((-1, chunksize))
        f_11chunks = f_11[:chunksize*numchunks].reshape((-1, chunksize))
        pb_11 = p_11chunks.mean(axis=1)
        fb_11 = f_11chunks.mean(axis=1)
        if len(p_11) > chunksize*numchunks:
           p_11_edge = p_11[range(chunksize*numchunks,len(p_11))]
           pb_11_edge = np.array([p_11_edge.mean()])  
           pb_11 = np.concatenate((pb_11,pb_11_edge), axis=0)
           f_11_edge = f_11[range(chunksize*numchunks,len(f_11))]
           fb_11_edge = np.array([f_11_edge.mean()])  
           fb_11 = np.concatenate((fb_11,fb_11_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-CS_MAG_LVEA_INPUTOPTICS_Y_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-EX_MAG_VEA_FLOOR_X_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '-EX_MAG_VEA_FLOOR_Y_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magexcasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_MAG_' in x_n:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            rng59_61 = range(30464,30976)
            p59_61 = np.sqrt(Pxx[rng59_61])
#            if np.sqrt(sum(p10_100)*1/512) < disconnect_magmainsmon_th and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magasdat60hz:
            if np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) < magasdat60hz:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0
        
        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = np.sqrt(sum(pb_10))/np.sqrt(sum(prb_10))
	pc_11 = np.sqrt(sum(pb_11))/np.sqrt(sum(prb_11))

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_2097153_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,fb_10,fb_11,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11)

#        if status == 'Ok' or status == 'Alert':        
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'
        
        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_for_4194305_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng11n = range(1536000,4194304)

        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9]; p_9 = Pxx[rng9]
        f_10 = freq[rng10]; p_10 = Pxx[rng10]
        f_11 = freq[rng11n]; p_11 = Pxx[rng11n]
        rng11a = range(3000*512,4000*512)
        rng11b = range(4000*512,5000*512)
        rng11c = range(5000*512,6000*512)
        rng11d = range(6000*512,7000*512)
        rng11e = range(7000*512,8192*512)
        f_11a = freq[rng11a]; p_11a = Pxx[rng11a]
        f_11b = freq[rng11b]; p_11b = Pxx[rng11b]
        f_11c = freq[rng11c]; p_11c = Pxx[rng11c]
        f_11d = freq[rng11d]; p_11d = Pxx[rng11d]
        f_11e = freq[rng11e]; p_11e = Pxx[rng11e]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]; prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:721]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        chunksize = 10000
        numchunks = p_10.size // chunksize 
        p_10chunks = p_10[:chunksize*numchunks].reshape((-1, chunksize))
        f_10chunks = f_10[:chunksize*numchunks].reshape((-1, chunksize))
        pb_10 = p_10chunks.mean(axis=1)
        fb_10 = f_10chunks.mean(axis=1)
        if len(p_10) > chunksize*numchunks:
           p_10_edge = p_10[range(chunksize*numchunks,len(p_10))]
           pb_10_edge = np.array([p_10_edge.mean()])  
           pb_10 = np.concatenate((pb_10,pb_10_edge), axis=0)
           f_10_edge = f_10[range(chunksize*numchunks,len(f_10))]
           fb_10_edge = np.array([f_10_edge.mean()])  
           fb_10 = np.concatenate((fb_10,fb_10_edge), axis=0)

        chunksize = 100000
        numchunks = p_11.size // chunksize 
        p_11chunks = p_11[:chunksize*numchunks].reshape((-1, chunksize))
        f_11chunks = f_11[:chunksize*numchunks].reshape((-1, chunksize))
        pb_11 = p_11chunks.mean(axis=1)
        fb_11 = f_11chunks.mean(axis=1)
        if len(p_11) > chunksize*numchunks:
           p_11_edge = p_11[range(chunksize*numchunks,len(p_11))]
           pb_11_edge = np.array([p_11_edge.mean()])  
           pb_11 = np.concatenate((pb_11,pb_11_edge), axis=0)
           f_11_edge = f_11[range(chunksize*numchunks,len(f_11))]
           fb_11_edge = np.array([f_11_edge.mean()])  
           fb_11 = np.concatenate((fb_11,fb_11_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'
        
        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = np.sqrt(sum(pb_10))/np.sqrt(sum(prb_10))
	pc_11 = np.sqrt(sum(pb_11))/np.sqrt(sum(prb_11))

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_4194305_and_allother_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11a,f_11b,f_11c,f_11d,f_11e,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11a,p_11b,p_11c,p_11d,p_11e,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,fb_10,fb_11,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour

def do_all_other_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs,freq,Pxx,Pxx_r):
        rng11n = range(1536000,5120000)
# Note: 16384Hz channels will be cut at 10,000Hz!!
        f_1 = freq[rng1]; p_1 = Pxx[rng1]
        f_2 = freq[rng2]; p_2 = Pxx[rng2]
        f_3 = freq[rng3]; p_3 = Pxx[rng3]
        f_4 = freq[rng4]; p_4 = Pxx[rng4]
        f_5 = freq[rng5]; p_5 = Pxx[rng5]
        f_6 = freq[rng6]; p_6 = Pxx[rng6]
        f_7 = freq[rng7]; p_7 = Pxx[rng7]
        f_8 = freq[rng8]; p_8 = Pxx[rng8]
        f_9 = freq[rng9]; p_9 = Pxx[rng9]
        f_10 = freq[rng10]; p_10 = Pxx[rng10]
        f_11 = freq[rng11n]; p_11 = Pxx[rng11n]
        rng11a = range(3000*512,4000*512)
        rng11b = range(4000*512,5000*512)
        rng11c = range(5000*512,6000*512)
        rng11d = range(6000*512,7000*512)
        rng11e = range(7000*512,10000*512)
        f_11a = freq[rng11a]; p_11a = Pxx[rng11a]
        f_11b = freq[rng11b]; p_11b = Pxx[rng11b]
        f_11c = freq[rng11c]; p_11c = Pxx[rng11c]
        f_11d = freq[rng11d]; p_11d = Pxx[rng11d]
        f_11e = freq[rng11e]; p_11e = Pxx[rng11e]

        pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]; prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]
        prb_6 = Pxx_r[313:416]; prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]; prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:730]

        chunksize = 10
        numchunks = p_3.size // chunksize 
        p_3chunks = p_3[:chunksize*numchunks].reshape((-1, chunksize))
        f_3chunks = f_3[:chunksize*numchunks].reshape((-1, chunksize))
        pb_3 = p_3chunks.mean(axis=1)
        fb_3 = f_3chunks.mean(axis=1)
        if len(p_3) > chunksize*numchunks:
           p_3_edge = p_3[range(chunksize*numchunks,len(p_3))]
           pb_3_edge = np.array([p_3_edge.mean()])  
           pb_3 = np.concatenate((pb_3,pb_3_edge), axis=0)
           f_3_edge = f_3[range(chunksize*numchunks,len(f_3))]
           fb_3_edge = np.array([f_3_edge.mean()])  
           fb_3 = np.concatenate((fb_3,fb_3_edge), axis=0)

        chunksize = 10
        numchunks = p_4.size // chunksize 
        p_4chunks = p_4[:chunksize*numchunks].reshape((-1, chunksize))
        f_4chunks = f_4[:chunksize*numchunks].reshape((-1, chunksize))
        pb_4 = p_4chunks.mean(axis=1)
        fb_4 = f_4chunks.mean(axis=1)
        if len(p_4) > chunksize*numchunks:
           p_4_edge = p_4[range(chunksize*numchunks,len(p_4))]
           pb_4_edge = np.array([p_4_edge.mean()])  
           pb_4 = np.concatenate((pb_4,pb_4_edge), axis=0)
           f_4_edge = f_4[range(chunksize*numchunks,len(f_4))]
           fb_4_edge = np.array([f_4_edge.mean()])  
           fb_4 = np.concatenate((fb_4,fb_4_edge), axis=0)

        chunksize = 100
        numchunks = p_5.size // chunksize 
        p_5chunks = p_5[:chunksize*numchunks].reshape((-1, chunksize))
        f_5chunks = f_5[:chunksize*numchunks].reshape((-1, chunksize))
        pb_5 = p_5chunks.mean(axis=1)
        fb_5 = f_5chunks.mean(axis=1)
        if len(p_5) > chunksize*numchunks:
           p_5_edge = p_5[range(chunksize*numchunks,len(p_5))]
           pb_5_edge = np.array([p_5_edge.mean()])  
           pb_5 = np.concatenate((pb_5,pb_5_edge), axis=0)
           f_5_edge = f_5[range(chunksize*numchunks,len(f_5))]
           fb_5_edge = np.array([f_5_edge.mean()])  
           fb_5 = np.concatenate((fb_5,fb_5_edge), axis=0)

        chunksize = 100
        numchunks = p_6.size // chunksize 
        p_6chunks = p_6[:chunksize*numchunks].reshape((-1, chunksize))
        f_6chunks = f_6[:chunksize*numchunks].reshape((-1, chunksize))
        pb_6 = p_6chunks.mean(axis=1)
        fb_6 = f_6chunks.mean(axis=1)
        if len(p_6) > chunksize*numchunks:
           p_6_edge = p_6[range(chunksize*numchunks,len(p_6))]
           pb_6_edge = np.array([p_6_edge.mean()])  
           pb_6 = np.concatenate((pb_6,pb_6_edge), axis=0)
           f_6_edge = f_6[range(chunksize*numchunks,len(f_6))]
           fb_6_edge = np.array([f_6_edge.mean()])  
           fb_6 = np.concatenate((fb_6,fb_6_edge), axis=0)

        chunksize = 1000
        numchunks = p_7.size // chunksize 
        p_7chunks = p_7[:chunksize*numchunks].reshape((-1, chunksize))
        f_7chunks = f_7[:chunksize*numchunks].reshape((-1, chunksize))
        pb_7 = p_7chunks.mean(axis=1)
        fb_7 = f_7chunks.mean(axis=1)
        if len(p_7) > chunksize*numchunks:
           p_7_edge = p_7[range(chunksize*numchunks,len(p_7))]
           pb_7_edge = np.array([p_7_edge.mean()])  
           pb_7 = np.concatenate((pb_7,pb_7_edge), axis=0)
           f_7_edge = f_7[range(chunksize*numchunks,len(f_7))]
           fb_7_edge = np.array([f_7_edge.mean()])  
           fb_7 = np.concatenate((fb_7,fb_7_edge), axis=0)

        chunksize = 1000
        numchunks = p_8.size // chunksize 
        p_8chunks = p_8[:chunksize*numchunks].reshape((-1, chunksize))
        f_8chunks = f_8[:chunksize*numchunks].reshape((-1, chunksize))
        pb_8 = p_8chunks.mean(axis=1)
        fb_8 = f_8chunks.mean(axis=1)
        if len(p_8) > chunksize*numchunks:
           p_8_edge = p_8[range(chunksize*numchunks,len(p_8))]
           pb_8_edge = np.array([p_8_edge.mean()])  
           pb_8 = np.concatenate((pb_8,pb_8_edge), axis=0)
           f_8_edge = f_8[range(chunksize*numchunks,len(f_8))]
           fb_8_edge = np.array([f_8_edge.mean()])  
           fb_8 = np.concatenate((fb_8,fb_8_edge), axis=0)

        chunksize = 10000
        numchunks = p_9.size // chunksize 
        p_9chunks = p_9[:chunksize*numchunks].reshape((-1, chunksize))
        f_9chunks = f_9[:chunksize*numchunks].reshape((-1, chunksize))
        pb_9 = p_9chunks.mean(axis=1)
        fb_9 = f_9chunks.mean(axis=1)
        if len(p_9) > chunksize*numchunks:
           p_9_edge = p_9[range(chunksize*numchunks,len(p_9))]
           pb_9_edge = np.array([p_9_edge.mean()])  
           pb_9 = np.concatenate((pb_9,pb_9_edge), axis=0)
           f_9_edge = f_9[range(chunksize*numchunks,len(f_9))]
           fb_9_edge = np.array([f_9_edge.mean()])  
           fb_9 = np.concatenate((fb_9,fb_9_edge), axis=0)

        chunksize = 10000
        numchunks = p_10.size // chunksize 
        p_10chunks = p_10[:chunksize*numchunks].reshape((-1, chunksize))
        f_10chunks = f_10[:chunksize*numchunks].reshape((-1, chunksize))
        pb_10 = p_10chunks.mean(axis=1)
        fb_10 = f_10chunks.mean(axis=1)
        if len(p_10) > chunksize*numchunks:
           p_10_edge = p_10[range(chunksize*numchunks,len(p_10))]
           pb_10_edge = np.array([p_10_edge.mean()])  
           pb_10 = np.concatenate((pb_10,pb_10_edge), axis=0)
           f_10_edge = f_10[range(chunksize*numchunks,len(f_10))]
           fb_10_edge = np.array([f_10_edge.mean()])  
           fb_10 = np.concatenate((fb_10,fb_10_edge), axis=0)

        chunksize = 100000
        numchunks = p_11.size // chunksize 
        p_11chunks = p_11[:chunksize*numchunks].reshape((-1, chunksize))
        f_11chunks = f_11[:chunksize*numchunks].reshape((-1, chunksize))
        pb_11 = p_11chunks.mean(axis=1)
        fb_11 = f_11chunks.mean(axis=1)
        if len(p_11) > chunksize*numchunks:
           p_11_edge = p_11[range(chunksize*numchunks,len(p_11))]
           pb_11_edge = np.array([p_11_edge.mean()])  
           pb_11 = np.concatenate((pb_11,pb_11_edge), axis=0)
           f_11_edge = f_11[range(chunksize*numchunks,len(f_11))]
           fb_11_edge = np.array([f_11_edge.mean()])  
           fb_11 = np.concatenate((fb_11,fb_11_edge), axis=0)

        p_1_new = p_1.reshape((-1,36))
        p_2_new = p_2.reshape((-1,102))
        pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11), axis=0)
        Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

        if '_SEIS_' in x_n:
            rng_seis = range(3*512,30*512+1)
            p_seis = Pxx[rng_seis]
            if np.sqrt(sum(p_seis)*1/512) < disconnect_seis_th and np.amin(np.sqrt(p_seis)) > comb_seis_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p_seis)) < comb_seis_th:
                       comb = 'Yes'
            else:      comb = 'No'

        elif '_ACC_' in x_n or '_MIC_' in x_n:
            rng10_300 = range(10*512,59*512+1) + range(61*512,119*512+1) + range(121*512,179*512+1) + range(181*512,239*512+1) + range(241*512,299*512+1)
            p10_300 = Pxx[rng10_300]
            if np.sqrt(sum(p10_300)*1/512) < disconnect_accmic_th and np.amin(np.sqrt(p10_300)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_300)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        else:
            rng10_59 = range(10*512,59*512+1)
            rng61_100 = range(61*512,100*512+1)
            rng10_100 = rng10_59 + rng61_100
            p10_100 = Pxx[rng10_100]
            if np.sqrt(sum(p10_100)*1/512) < disconnect_th and np.amin(np.sqrt(p10_100)) > comb_th:
                       disconnect = 'Yes'
            else:      disconnect = 'No'

            if np.amin(np.sqrt(p10_100)) < comb_th:
                       comb = 'Yes'
            else:      comb = 'No'

        
        if  disconnect == 'Yes':
            disconhour = get_disconnected_yes_hour(x_n)
        else:
            disconhour = 0

        if  comb == 'Yes':
            daqfailhour = get_daqfailure_yes_hour(x_n)
        else:
            daqfailhour = 0

        pc_1 = np.sqrt(sum(p_1))/np.sqrt(sum(pr_1))
        pc_2 = np.sqrt(sum(p_2))/np.sqrt(sum(pr_2))
	pc_3 = np.sqrt(sum(pb_3))/np.sqrt(sum(prb_3))
	pc_4 = np.sqrt(sum(pb_4))/np.sqrt(sum(prb_4))
	pc_5 = np.sqrt(sum(pb_5))/np.sqrt(sum(prb_5))
	pc_6 = np.sqrt(sum(pb_6))/np.sqrt(sum(prb_6))
	pc_7 = np.sqrt(sum(pb_7))/np.sqrt(sum(prb_7))
	pc_8 = np.sqrt(sum(pb_8))/np.sqrt(sum(prb_8))
	pc_9 = np.sqrt(sum(pb_9))/np.sqrt(sum(prb_9))
	pc_10 = np.sqrt(sum(pb_10))/np.sqrt(sum(prb_10))
	pc_11 = np.sqrt(sum(pb_11))/np.sqrt(sum(prb_11))

        if '_SEIS_' in x_n:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        elif '_ACC_' in x_n or '_MIC_' in x_n:
	        pc_list_2 = [pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        else:
	        pc_list_1 = [pc_1,pc_2,pc_3]
	        pc_list_2 = [pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11]
	        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
	        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]  
	        if not cond_1 and not cond_2:
                    excess = 'No'
	        else:
                    excess = 'Yes'
        if comb == 'Yes' or disconnect == 'Yes':
#        if comb == 'Yes' or excess == 'Yes' or disconnect == 'Yes':
                                                                   status = 'Alert'
        else:
                                                                   status = 'Ok'  

        pltutils.timeseries_plot(x_n,x_nn,strcurGpsTime,strcurUtcTime,data,Fs)
        pltutils.psdplot_4194305_and_allother_case(x_n,x_nn,strcurGpsTime,strcurUtcTime,Fs,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9,f_10,f_11a,f_11b,f_11c,f_11d,f_11e,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8,p_9,p_10,p_11a,p_11b,p_11c,p_11d,p_11e,fb_3,fb_4,fb_5,fb_6,fb_7,fb_8,fb_9,fb_10,fb_11,pb_3,pb_4,pb_5,pb_6,pb_7,pb_8,pb_9,pb_10,pb_11,pr_1,pr_2,prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11)

#        if status == 'Ok' or status == 'Alert':
        if status == 'Ok': 
           newreffile = open(run_dir + 'ref_files/'+x_nn+'.txt', 'w')
           for item in Pxx_r_new:
                      print>>newreffile, item
           newreffile.close()
        else:
           print 'Not saving spectra'

        return pc_1,pc_2,pc_3,pc_4,pc_5,pc_6,pc_7,pc_8,pc_9,pc_10,pc_11,excess,comb,disconnect,status,disconhour,daqfailhour


