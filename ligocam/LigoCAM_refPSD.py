from __future__ import division
import matplotlib.mlab as mlab
import LigoCAM_refutils as LCrefutils
from glue import lal
from pylal import frutils

alpha = 2 / (1+12)

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

def get_binned(x_n, refstart, refend, Pxx_len, Fs, overlap):
    file_prefix_ri = run_dir + 'cache/reference_' + str(refstart) + '_'
    cache_file_ri = file_prefix_ri + 'frame_cache.txt'
    cache_ri = lal.Cache.fromfile(open(cache_file_ri))
    get_data_ri = frutils.FrameCache(cache_ri, scratchdir=None, verbose=False)
    data_ri = get_data_ri.fetch(x_n, refstart, refend)
    Pxx_ri, freq_ri = mlab.psd(data_ri, NFFT=len(data_ri), Fs=int(Fs), \
                          noverlap=int(overlap*Fs), detrend=mlab.detrend_none, \
                          window=mlab.window_hanning, pad_to=None, \
                          sides='default', scale_by_freq=1)
    if Pxx_len == 4097:
        Pxx_ref_binned = LCrefutils.do_all_for_4097_case(Pxx_ri)
    elif Pxx_len == 8193:
        Pxx_ref_binned = LCrefutils.do_all_for_8193_case(Pxx_ri)
    elif Pxx_len == 16385:
        Pxx_ref_binned = LCrefutils.do_all_for_16385_case(Pxx_ri)
    elif Pxx_len == 32769:
        Pxx_ref_binned = LCrefutils.do_all_for_32769_case(Pxx_ri)
    elif Pxx_len == 65537:
        Pxx_ref_binned = LCrefutils.do_all_for_65537_case(Pxx_ri)
    elif Pxx_len == 131073:
        Pxx_ref_binned = LCrefutils.do_all_for_131073_case(Pxx_ri)
    elif Pxx_len == 262145:
        Pxx_ref_binned = LCrefutils.do_all_for_262145_case(Pxx_ri)
    elif Pxx_len == 524289:
        Pxx_ref_binned = LCrefutils.do_all_for_524289_case(Pxx_ri)
    elif Pxx_len == 1048577:
        Pxx_ref_binned = LCrefutils.do_all_for_1048577_case(Pxx_ri)
    elif Pxx_len == 2097153:
        Pxx_ref_binned = LCrefutils.do_all_for_2097153_case(Pxx_ri)
    elif Pxx_len == 4194305:
        Pxx_ref_binned = LCrefutils.do_all_for_4194305_case(Pxx_ri)
    else:
        Pxx_ref_binned = LCrefutils.do_all_other_case(Pxx_ri)
    return Pxx_ref_binned

def compute_refpsd(x_n, x_nn, gpsstarttime, Pxx_len, observatory, frame_type, \
                                                                Fs, overlap):
    refstart1 = gpsstarttime - 3600
    refend1 =  refstart1 + 512
    Pxx_r1_binned = get_binned(x_n, refstart1, refend1, Pxx_len, Fs, overlap)

    refstart2 = refstart1 - 3600
    refend2 =  refstart2 + 512
    Pxx_r2_binned = get_binned(x_n, refstart2, refend2, Pxx_len, Fs, overlap)

    refstart3 = refstart2 - 3600
    refend3 =  refstart3 + 512
    Pxx_r3_binned = get_binned(x_n, refstart3, refend3, Pxx_len, Fs, overlap)

    refstart4 = refstart3 - 3600
    refend4 =  refstart4 + 512
    Pxx_r4_binned = get_binned(x_n, refstart4, refend4, Pxx_len, Fs, overlap)

    refstart5 = refstart4 - 3600
    refend5 =  refstart5 + 512
    Pxx_r5_binned = get_binned(x_n, refstart5, refend5, Pxx_len, Fs, overlap)

    refstart6 = refstart5 - 3600
    refend6 =  refstart6 + 512
    Pxx_r6_binned = get_binned(x_n, refstart6, refend6, Pxx_len, Fs, overlap)

    refstart7 = refstart6 - 3600
    refend7 =  refstart7 + 512
    Pxx_r7_binned = get_binned(x_n, refstart7, refend7, Pxx_len, Fs, overlap)

    refstart8 = refstart7 - 3600
    refend8 =  refstart8 + 512
    Pxx_r8_binned = get_binned(x_n, refstart8, refend8, Pxx_len, Fs, overlap)

    refstart9 = refstart8 - 3600
    refend9 =  refstart9 + 512
    Pxx_r9_binned = get_binned(x_n, refstart9, refend9, Pxx_len, Fs, overlap)

    refstart10 = refstart9 - 3600
    refend10 =  refstart10 + 512
    Pxx_r10_binned = get_binned(x_n, refstart10, refend10, Pxx_len, Fs, overlap)

    refstart11 = refstart10 - 3600
    refend11 =  refstart11 + 512
    Pxx_r11_binned = get_binned(x_n, refstart11, refend11, Pxx_len, Fs, overlap)

    refstart12 = refstart11 - 3600
    refend12 =  refstart12 + 512
    Pxx_r12_binned = get_binned(x_n, refstart12, refend12, Pxx_len, Fs, overlap)

    simple_mean = (Pxx_r1_binned + Pxx_r2_binned) / 2
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
