from __future__ import division

#from numpy import *
#from pylab import *
#import matplotlib.pyplot as plt
#from matplotlib.mlab import *
import matplotlib.mlab as mlab
#from scipy import stats
#import os, sys, commands
#import nds2
#from optparse import OptionParser
import LigoCAM_refutils as LCrefutils
#import shutil
from glue import lal
from pylal import frutils

alpha = 2/(1+12)

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

def compute_refpsd(x_n,x_nn,gpsstarttime,Pxx_len,observatory,frame_type,Fs,overlap):

       refgpsstat1 = gpsstarttime - 3600
       refgpsend1 =  refgpsstat1 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat1) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat1,refgpsend1)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r1_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r1_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r1_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r1_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r1_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r1_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r1_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r1_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r1_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r1_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r1_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r1_binned = LCrefutils.do_all_other_case(Pxx_ri)
       

       refgpsstat2 = refgpsstat1 - 3600
       refgpsend2 =  refgpsstat2 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat2) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat2,refgpsend2)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r2_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r2_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r2_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r2_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r2_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r2_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r2_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r2_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r2_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r2_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r2_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r2_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat3 = refgpsstat2 - 3600
       refgpsend3 =  refgpsstat3 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat3) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat3,refgpsend3)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r3_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r3_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r3_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r3_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r3_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r3_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r3_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r3_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r3_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r3_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r3_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r3_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat4 = refgpsstat3 - 3600
       refgpsend4 =  refgpsstat4 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat4) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat4,refgpsend4)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r4_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r4_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r4_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r4_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r4_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r4_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r4_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r4_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r4_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r4_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r4_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r4_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat5 = refgpsstat4 - 3600
       refgpsend5 =  refgpsstat5 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat5) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat5,refgpsend5)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r5_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r5_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r5_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r5_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r5_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r5_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r5_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r5_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r5_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r5_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r5_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r5_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat6 = refgpsstat5 - 3600
       refgpsend6 =  refgpsstat6 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat6) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat6,refgpsend6)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r6_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r6_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r6_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r6_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r6_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r6_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r6_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r6_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r6_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r6_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r6_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r6_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat7 = refgpsstat6 - 3600
       refgpsend7 =  refgpsstat7 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat7) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat7,refgpsend7)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r7_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r7_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r7_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r7_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r7_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r7_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r7_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r7_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r7_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r7_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r7_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r7_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat8 = refgpsstat7 - 3600
       refgpsend8 =  refgpsstat8 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat8) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat8,refgpsend8)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r8_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r8_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r8_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r8_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r8_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r8_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r8_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r8_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r8_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r8_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r8_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r8_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat9 = refgpsstat8 - 3600
       refgpsend9 =  refgpsstat9 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat9) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat9,refgpsend9)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r9_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r9_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r9_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r9_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r9_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r9_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r9_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r9_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r9_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r9_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r9_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r9_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat10 = refgpsstat9 - 3600
       refgpsend10 =  refgpsstat10 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat10) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat10,refgpsend10)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r10_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r10_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r10_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r10_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r10_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r10_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r10_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r10_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r10_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r10_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r10_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r10_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat11 = refgpsstat10 - 3600
       refgpsend11 =  refgpsstat11 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat11) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat11,refgpsend11)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r11_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r11_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r11_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r11_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r11_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r11_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r11_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r11_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r11_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r11_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r11_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r11_binned = LCrefutils.do_all_other_case(Pxx_ri)


       refgpsstat12 = refgpsstat11 - 3600
       refgpsend12 =  refgpsstat12 + 512
       file_prefix_ri = run_dir + 'cache/reference_' + str(refgpsstat12) + '_'
       cache_file_ri = file_prefix_ri + 'frame_cache.txt'
       cache_ri = lal.Cache.fromfile(open(cache_file_ri))
       get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
       data_ri = get_data_ri.fetch(x_n,refgpsstat12,refgpsend12)
       Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), noverlap=int(overlap*Fs), detrend=mlab.detrend_none, window=mlab.window_hanning, pad_to=None, sides='default', scale_by_freq=1)
       if Pxx_len == 4097:
          Pxx_r12_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
       elif Pxx_len == 8193:
          Pxx_r12_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
       elif Pxx_len == 16385:
          Pxx_r12_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
       elif Pxx_len == 32769:
          Pxx_r12_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
       elif Pxx_len == 65537:
          Pxx_r12_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
       elif Pxx_len == 131073:
          Pxx_r12_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
       elif Pxx_len == 262145:
          Pxx_r12_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
       elif Pxx_len == 524289:
          Pxx_r12_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
       elif Pxx_len == 1048577:
          Pxx_r12_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
       elif Pxx_len == 2097153:
          Pxx_r12_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
       elif Pxx_len == 4194305:
          Pxx_r12_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
       else:
          Pxx_r12_binned = LCrefutils.do_all_other_case(Pxx_ri)

   
       simple_mean = (Pxx_r1_binned+Pxx_r2_binned)/2
       ema3 = simple_mean + alpha * (Pxx_r3_binned - simple_mean)
       ema4 = ema3 + alpha * (Pxx_r4_binned - ema3)
       ema5 = ema4 + alpha * (Pxx_r5_binned - ema4)
       ema6 = ema5 + alpha * (Pxx_r6_binned - ema5)
       ema7 = ema6 + alpha * (Pxx_r7_binned - ema6)
       ema8 = ema7 + alpha * (Pxx_r8_binned - ema7)
       ema9 = ema8 + alpha * (Pxx_r9_binned - ema8)
       ema10 = ema9 + alpha * (Pxx_r10_binned - ema9)
       ema11 = ema10 + alpha * (Pxx_r11_binned - ema10)
       ema12 = ema11 + alpha * (Pxx_r12_binned - ema11)       

       Pxx_r = ema12

       return Pxx_r












