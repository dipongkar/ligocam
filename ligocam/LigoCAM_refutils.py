from __future__ import division
import numpy as np

rng1 = range(16, 52)
rng2 = range(52, 154)
rng3 = range(154, 512)
rng4 = range(512, 1536)
rng5 = range(1536, 5120)
rng6 = range(5120, 15360)
rng7 = range(15360, 51200)
rng8 = range(51200, 153600)
rng9 = range(153600, 512000)
rng10 = range(512000, 1536000)

def get_binned_refpsd(refpsd, chunksize):
    numchunks = refpsd.size // chunksize
    refpsd_chunks = refpsd[:chunksize * numchunks].reshape((-1, chunksize))
    refpsd_binned = refpsd_chunks.mean(axis=1)
    if len(refpsd) > chunksize * numchunks:
        refpsd_edge = refpsd[range(chunksize * numchunks, len(refpsd))]
        refpsd_binned_edge = np.array([refpsd_edge.mean()])
        refpsd_binned = np.concatenate((refpsd_binned, refpsd_binned_edge), \
                                                                      axis=0)
    return refpsd_binned

def do_all_for_4097_case(Pxx_ri):
    rng5n = range(1536, 4096)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                                              prb_5), axis=0)
    return Pxx_ri_binned

def do_all_for_8193_case(Pxx_ri):
    rng6n = range(5120, 8192)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                                       prb_5, prb_6), axis=0)
    return Pxx_ri_binned

def do_all_for_16385_case(Pxx_ri):
    rng7n = range(15360, 16384)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6]
    pr_7 = Pxx_ri[rng7n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                                prb_5, prb_6, prb_7), axis=0)
    return Pxx_ri_binned

def do_all_for_32769_case(Pxx_ri):
    rng7n = range(15360, 32768)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6]
    pr_7 = Pxx_ri[rng7n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                                prb_5, prb_6, prb_7), axis=0)
    return Pxx_ri_binned

def do_all_for_65537_case(Pxx_ri):
    rng8n = range(51200, 65536)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6]
    pr_7 = Pxx_ri[rng7]
    pr_8 = Pxx_ri[rng8n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                         prb_5, prb_6, prb_7, prb_8), axis=0)
    return Pxx_ri_binned

def do_all_for_131073_case(Pxx_ri):
    rng8n = range(51200, 131072)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6]
    pr_7 = Pxx_ri[rng7]
    pr_8 = Pxx_ri[rng8n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                         prb_5, prb_6, prb_7, prb_8), axis=0)
    return Pxx_ri_binned

def do_all_for_262145_case(Pxx_ri):
    rng9n = range(153600, 262144)
    pr_1 = Pxx_ri[rng1]
    pr_2 = Pxx_ri[rng2]
    pr_3 = Pxx_ri[rng3]
    pr_4 = Pxx_ri[rng4]
    pr_5 = Pxx_ri[rng5]
    pr_6 = Pxx_ri[rng6]
    pr_7 = Pxx_ri[rng7]
    pr_8 = Pxx_ri[rng8]
    pr_9 = Pxx_ri[rng9n]

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                                  prb_5, prb_6, prb_7, prb_8, prb_9), axis=0)
    return Pxx_ri_binned

def do_all_for_524289_case(Pxx_ri):
    rng10n = range(512000, 524288)
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

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)
    prb_10 = get_binned_refpsd(pr_10, 10000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                          prb_5, prb_6, prb_7, prb_8, prb_9, prb_10), axis=0)
    return Pxx_ri_binned

def do_all_for_1048577_case(Pxx_ri):
    rng10n = range(512000, 1048576)
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

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)
    prb_10 = get_binned_refpsd(pr_10, 10000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                          prb_5, prb_6, prb_7, prb_8, prb_9, prb_10), axis=0)
    return Pxx_ri_binned

def do_all_for_2097153_case(Pxx_ri):
    rng11n = range(1536000, 2097152)
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

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)
    prb_10 = get_binned_refpsd(pr_10, 10000)
    prb_11 = get_binned_refpsd(pr_11, 100000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                   prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11), axis=0)
    return Pxx_ri_binned

def do_all_for_4194305_case(Pxx_ri):
    rng11n = range(1536000, 4194304)
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

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)
    prb_10 = get_binned_refpsd(pr_10, 10000)
    prb_11 = get_binned_refpsd(pr_11, 100000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                   prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11), axis=0)
    return Pxx_ri_binned

def do_all_other_case(Pxx_ri):
    rng11n = range(1536000, 5120000)
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

    prb_3 = get_binned_refpsd(pr_3, 10)
    prb_4 = get_binned_refpsd(pr_4, 10)
    prb_5 = get_binned_refpsd(pr_5, 100)
    prb_6 = get_binned_refpsd(pr_6, 100)
    prb_7 = get_binned_refpsd(pr_7, 1000)
    prb_8 = get_binned_refpsd(pr_8, 1000)
    prb_9 = get_binned_refpsd(pr_9, 10000)
    prb_10 = get_binned_refpsd(pr_10, 10000)
    prb_11 = get_binned_refpsd(pr_11, 100000)

    pr_1_new = pr_1.reshape((-1, 36))
    pr_2_new = pr_2.reshape((-1, 102))
    Pxx_ri_binned = np.concatenate((pr_1_new[0], pr_2_new[0], prb_3, prb_4, \
                   prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11), axis=0)
    return Pxx_ri_binned
