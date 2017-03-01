from __future__ import division
#from numpy import *
import numpy as np
#from pylab import *
#import matplotlib.pyplot as plt
#from matplotlib.mlab import *
#from scipy import stats
#from pylal import frutils
#from glue import lal
#import os
#import nds2
#from optparse import OptionParser

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

def do_all_for_4097_case(Pxx_ri):
        rng5n = range(1536,4096)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0)  

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5), axis=0)

        return Pxx_ri_binned

def do_all_for_8193_case(Pxx_ri):
        rng6n = range(5120,8192)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6), axis=0)

        return Pxx_ri_binned

def do_all_for_16385_case(Pxx_ri):
        rng7n = range(15360,16384)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7), axis=0)

        return Pxx_ri_binned

def do_all_for_32769_case(Pxx_ri):
        rng7n = range(15360,32768)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7), axis=0)

        return Pxx_ri_binned

def do_all_for_65537_case(Pxx_ri):
        rng8n = range(51200,65536)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8), axis=0)

        return Pxx_ri_binned

def do_all_for_131073_case(Pxx_ri):
        rng8n = range(51200,131072)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8), axis=0)

        return Pxx_ri_binned

def do_all_for_262145_case(Pxx_ri):
        rng9n = range(153600,262144)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9), axis=0)

        return Pxx_ri_binned

def do_all_for_524289_case(Pxx_ri):
        rng10n = range(512000,524288)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9]
        pr_10 = Pxx_ri[rng10n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_10.size // chunksize 
        pr_10chunks = pr_10[:chunksize*numchunks].reshape((-1, chunksize))
        prb_10 = pr_10chunks.mean(axis=1)
        if len(pr_10) > chunksize*numchunks:
           pr_10_edge = pr_10[range(chunksize*numchunks,len(pr_10))]
           prb_10_edge = np.array([pr_10_edge.mean()])  
           prb_10 = np.concatenate((prb_10,prb_10_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10), axis=0)

        return Pxx_ri_binned

def do_all_for_1048577_case(Pxx_ri):
        rng10n = range(512000,1048576)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9]
        pr_10 = Pxx_ri[rng10n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_10.size // chunksize 
        pr_10chunks = pr_10[:chunksize*numchunks].reshape((-1, chunksize))
        prb_10 = pr_10chunks.mean(axis=1)
        if len(pr_10) > chunksize*numchunks:
           pr_10_edge = pr_10[range(chunksize*numchunks,len(pr_10))]
           prb_10_edge = np.array([pr_10_edge.mean()])  
           prb_10 = np.concatenate((prb_10,prb_10_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10), axis=0)

        return Pxx_ri_binned

def do_all_for_2097153_case(Pxx_ri):
        rng11n = range(1536000,2097152)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9]
        pr_10 = Pxx_ri[rng10]
        pr_11 = Pxx_ri[rng11n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_10.size // chunksize 
        pr_10chunks = pr_10[:chunksize*numchunks].reshape((-1, chunksize))
        prb_10 = pr_10chunks.mean(axis=1)
        if len(pr_10) > chunksize*numchunks:
           pr_10_edge = pr_10[range(chunksize*numchunks,len(pr_10))]
           prb_10_edge = np.array([pr_10_edge.mean()])  
           prb_10 = np.concatenate((prb_10,prb_10_edge), axis=0) 

        chunksize = 100000
        numchunks = pr_11.size // chunksize 
        pr_11chunks = pr_11[:chunksize*numchunks].reshape((-1, chunksize))
        prb_11 = pr_11chunks.mean(axis=1)
        if len(pr_11) > chunksize*numchunks:
           pr_11_edge = pr_11[range(chunksize*numchunks,len(pr_11))]
           prb_11_edge = np.array([pr_11_edge.mean()])  
           prb_11 = np.concatenate((prb_11,prb_11_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11), axis=0)

        return Pxx_ri_binned

def do_all_for_4194305_case(Pxx_ri):
        rng11n = range(1536000,4194304)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9]
        pr_10 = Pxx_ri[rng10]
        pr_11 = Pxx_ri[rng11n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0) 

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_10.size // chunksize 
        pr_10chunks = pr_10[:chunksize*numchunks].reshape((-1, chunksize))
        prb_10 = pr_10chunks.mean(axis=1)
        if len(pr_10) > chunksize*numchunks:
           pr_10_edge = pr_10[range(chunksize*numchunks,len(pr_10))]
           prb_10_edge = np.array([pr_10_edge.mean()])  
           prb_10 = np.concatenate((prb_10,prb_10_edge), axis=0) 

        chunksize = 100000
        numchunks = pr_11.size // chunksize 
        pr_11chunks = pr_11[:chunksize*numchunks].reshape((-1, chunksize))
        prb_11 = pr_11chunks.mean(axis=1)
        if len(pr_11) > chunksize*numchunks:
           pr_11_edge = pr_11[range(chunksize*numchunks,len(pr_11))]
           prb_11_edge = np.array([pr_11_edge.mean()])  
           prb_11 = np.concatenate((prb_11,prb_11_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11), axis=0)

        return Pxx_ri_binned

def do_all_other_case(Pxx_ri):
        rng11n = range(1536000,5120000)

        pr_1 = Pxx_ri[rng1]
        pr_2 = Pxx_ri[rng2]
        pr_3 = Pxx_ri[rng3]
        pr_4 = Pxx_ri[rng4]
        pr_5 = Pxx_ri[rng5]
        pr_6 = Pxx_ri[rng6]
        pr_7 = Pxx_ri[rng7]
        pr_8 = Pxx_ri[rng8]
        pr_9 = Pxx_ri[rng9]
        pr_10 = Pxx_ri[rng10]
        pr_11 = Pxx_ri[rng11n]

        chunksize = 10
        numchunks = pr_3.size // chunksize 
        pr_3chunks = pr_3[:chunksize*numchunks].reshape((-1, chunksize))
        prb_3 = pr_3chunks.mean(axis=1)
        if len(pr_3) > chunksize*numchunks:
           pr_3_edge = pr_3[range(chunksize*numchunks,len(pr_3))]
           prb_3_edge = np.array([pr_3_edge.mean()])  
           prb_3 = np.concatenate((prb_3,prb_3_edge), axis=0) 

        chunksize = 10
        numchunks = pr_4.size // chunksize 
        pr_4chunks = pr_4[:chunksize*numchunks].reshape((-1, chunksize))
        prb_4 = pr_4chunks.mean(axis=1)
        if len(pr_4) > chunksize*numchunks:
           pr_4_edge = pr_4[range(chunksize*numchunks,len(pr_4))]
           prb_4_edge = np.array([pr_4_edge.mean()])  
           prb_4 = np.concatenate((prb_4,prb_4_edge), axis=0) 

        chunksize = 100
        numchunks = pr_5.size // chunksize 
        pr_5chunks = pr_5[:chunksize*numchunks].reshape((-1, chunksize))
        prb_5 = pr_5chunks.mean(axis=1)
        if len(pr_5) > chunksize*numchunks:
           pr_5_edge = pr_5[range(chunksize*numchunks,len(pr_5))]
           prb_5_edge = np.array([pr_5_edge.mean()])  
           prb_5 = np.concatenate((prb_5,prb_5_edge), axis=0)

        chunksize = 100
        numchunks = pr_6.size // chunksize 
        pr_6chunks = pr_6[:chunksize*numchunks].reshape((-1, chunksize))
        prb_6 = pr_6chunks.mean(axis=1)
        if len(pr_6) > chunksize*numchunks:
           pr_6_edge = pr_6[range(chunksize*numchunks,len(pr_6))]
           prb_6_edge = np.array([pr_6_edge.mean()])  
           prb_6 = np.concatenate((prb_6,prb_6_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_7.size // chunksize 
        pr_7chunks = pr_7[:chunksize*numchunks].reshape((-1, chunksize))
        prb_7 = pr_7chunks.mean(axis=1)
        if len(pr_7) > chunksize*numchunks:
           pr_7_edge = pr_7[range(chunksize*numchunks,len(pr_7))]
           prb_7_edge = np.array([pr_7_edge.mean()])  
           prb_7 = np.concatenate((prb_7,prb_7_edge), axis=0) 

        chunksize = 1000
        numchunks = pr_8.size // chunksize 
        pr_8chunks = pr_8[:chunksize*numchunks].reshape((-1, chunksize))
        prb_8 = pr_8chunks.mean(axis=1)
        if len(pr_8) > chunksize*numchunks:
           pr_8_edge = pr_8[range(chunksize*numchunks,len(pr_8))]
           prb_8_edge = np.array([pr_8_edge.mean()])  
           prb_8 = np.concatenate((prb_8,prb_8_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_9.size // chunksize 
        pr_9chunks = pr_9[:chunksize*numchunks].reshape((-1, chunksize))
        prb_9 = pr_9chunks.mean(axis=1)
        if len(pr_9) > chunksize*numchunks:
           pr_9_edge = pr_9[range(chunksize*numchunks,len(pr_9))]
           prb_9_edge = np.array([pr_9_edge.mean()])  
           prb_9 = np.concatenate((prb_9,prb_9_edge), axis=0) 

        chunksize = 10000
        numchunks = pr_10.size // chunksize 
        pr_10chunks = pr_10[:chunksize*numchunks].reshape((-1, chunksize))
        prb_10 = pr_10chunks.mean(axis=1)
        if len(pr_10) > chunksize*numchunks:
           pr_10_edge = pr_10[range(chunksize*numchunks,len(pr_10))]
           prb_10_edge = np.array([pr_10_edge.mean()])  
           prb_10 = np.concatenate((prb_10,prb_10_edge), axis=0) 

        chunksize = 100000
        numchunks = pr_11.size // chunksize 
        pr_11chunks = pr_11[:chunksize*numchunks].reshape((-1, chunksize))
        prb_11 = pr_11chunks.mean(axis=1)
        if len(pr_11) > chunksize*numchunks:
           pr_11_edge = pr_11[range(chunksize*numchunks,len(pr_11))]
           prb_11_edge = np.array([pr_11_edge.mean()])  
           prb_11 = np.concatenate((prb_11,prb_11_edge), axis=0) 

        pr_1_new = pr_1.reshape((-1,36))
        pr_2_new = pr_2.reshape((-1,102))
        Pxx_ri_binned = np.concatenate((pr_1_new[0],pr_2_new[0],prb_3,prb_4,prb_5,prb_6,prb_7,prb_8,prb_9,prb_10,prb_11), axis=0)

        return Pxx_ri_binned

