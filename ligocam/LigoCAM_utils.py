# Copyright (C) 2013 Dipongkar Talukder
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

""" This file is part of LIGO Channel Activity Monitor (LigoCAM)."""

from __future__ import division
import numpy as np
import LigoCAM_plotutils as pltutils

__author__ = 'Dipongkar Talukder <dipongkar.talukder@ligo.org>'

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
disconnect_seis_th = 0.1
disconnect_th = 2.0
disconnect_accmic_th = 1.2
disconnect_lowfmictemperature_th = 0.1
disconnect_tilt_th = 0.2
disconnect_magmainsmon_th = 0.2
disconnect_128hzmainsmon_th = 0.18
magasdat60hz = 1000
magexcasdat60hz = 100
mainsmonat60hz = 1000
thd1g = 1000; thd1l = 1/500
thd2g = 50; thd2l = 1/5

alpha = 2 / (1+12)

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

def get_disconnected_yes_hour(run_dir, x_n):
    ff = open(run_dir + '/results/Disconnected_past.txt', 'r')
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

def get_daqfailure_yes_hour(run_dir, x_n):
    ff = open(run_dir + '/results/DAQfailure_past.txt', 'r')
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

def get_binned_data(freq, pwr, chunksize):
    numchunks = pwr.size // chunksize
    pwr_chunks = pwr[:chunksize * numchunks].reshape((-1, chunksize))
    freq_chunks = freq[:chunksize * numchunks].reshape((-1, chunksize))
    pwr_binned = pwr_chunks.mean(axis=1)
    freq_binned = freq_chunks.mean(axis=1)
    if len(pwr) > chunksize * numchunks:
        pwr_edge = pwr[range(chunksize * numchunks, len(pwr))]
        pwr_binned_edge = np.array([pwr_edge.mean()])
        pwr_binned = np.concatenate((pwr_binned, pwr_binned_edge), axis=0)
        freq_edge = freq[range(chunksize * numchunks, len(freq))]
        freq_binned_edge = np.array([freq_edge.mean()])
        freq_binned = np.concatenate((freq_binned, freq_binned_edge), axis=0)
    return freq_binned, pwr_binned

def do_all_for_4097_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng5n = range(1536, 4096)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5n]; p_5 = Pxx[rng5n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:303]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5), axis=0)
    Pxx_r_new = Pxx_r + alpha*(pb_new - Pxx_r)

    rng0p3_5 = range(154, 5*512)
    p0p3_5 = Pxx[rng0p3_5]
    if np.sqrt(sum(p0p3_5) * 1/512) < disconnect_4097_case_th \
       and np.amin(np.sqrt(p0p3_5)) > comb_0p3to20hz_th:
        disconnect = 'Yes'
    else:
        disconnect = 'No'
    if np.amin(np.sqrt(p0p3_5)) < comb_0p3to20hz_th:
        comb = 'Yes'
    else:
        comb = 'No'
    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = 0
    pc_7 = 0
    pc_8 = 0
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_4097_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
                              f_1, f_2, f_3, f_4, f_5, p_1, p_2, p_3, p_4, \
                              p_5, fb_3, fb_4, fb_5, pb_3, pb_4, pb_5, pr_1, \
                                                  pr_2, prb_3, prb_4, prb_5)
    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_8193_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                               data, Fs, freq, Pxx, Pxx_r):
    rng6n = range(5120, 8192)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6n]; p_6 = Pxx[rng6n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:344]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6), \
                                                                     axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    rng0p3_10 = range(154, 10*512)
    p0p3_10 = Pxx[rng0p3_10]
    if np.sqrt(sum(p0p3_10) * 1/512) < disconnect_8193_case_th and \
       np.amin(np.sqrt(p0p3_10)) > comb_0p3to20hz_th:
        disconnect = 'Yes'
    else:
        disconnect = 'No'
    if np.amin(np.sqrt(p0p3_10)) < comb_0p3to20hz_th:
        comb = 'Yes'
    else:
        comb = 'No'
    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = 0
    pc_8 = 0
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_8193_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
                        f_1, f_2, f_3, f_4, f_5, f_6, p_1, p_2, p_3, p_4, p_5, \
                        p_6, fb_3, fb_4, fb_5, fb_6, pb_3, pb_4, pb_5, pb_6, \
                        pr_1, pr_2, prb_3, prb_4, prb_5, prb_6)
    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_16385_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng7n = range(15360, 16384)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6]; p_6 = Pxx[rng6]
    f_7 = freq[rng7n]; p_7 = Pxx[rng7n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:418]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0],p_2_new[0],pb_3,pb_4,pb_5,pb_6,pb_7), \
                                                                    axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    rng1_20 = range(512, 20*512)
    p1_20 = Pxx[rng1_20]
    if np.sqrt(sum(p1_20) * 1/512) < disconnect_16385_case_th \
       and np.amin(np.sqrt(p1_20)) > comb_0p3to20hz_th:
        disconnect = 'Yes'
    else:
        disconnect = 'No'

    if np.amin(np.sqrt(p1_20)) < comb_0p3to20hz_th:
        comb = 'Yes'
    else:
        comb = 'No'
    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = 0
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_16385_and_32769_case(run_dir, x_n, x_nn, strcurGpsTime, \
                      strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, \
                      p_1, p_2, p_3, p_4, p_5, p_6, p_7, fb_3, fb_4, fb_5, \
                      fb_6, fb_7, pb_3, pb_4, pb_5, pb_6, pb_7, pr_1, pr_2, \
                      prb_3, prb_4, prb_5, prb_6, prb_7)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_32769_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng7n = range(15360, 32768)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6]; p_6 = Pxx[rng6]
    f_7 = freq[rng7n]; p_7 = Pxx[rng7n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:434]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                                                pb_7), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    rng1_40 =range(512, 40*512)
    p1_40 = Pxx[rng1_40]
    if np.sqrt(sum(p1_40) * 1/512) < disconnect_32769_case_th \
       and np.amin(np.sqrt(p1_40)) > comb_1to40hz_th:
        disconnect = 'Yes'
    else:
        disconnect = 'No'
    if np.amin(np.sqrt(p1_40)) < comb_1to40hz_th:
        comb = 'Yes'
    else:
        comb = 'No'
    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = 0
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_16385_and_32769_case(run_dir, x_n, x_nn, strcurGpsTime, \
            strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, p_1, p_2, \
            p_3, p_4, p_5, p_6, p_7, fb_3, fb_4, fb_5, fb_6, fb_7, pb_3, pb_4, \
            pb_5, pb_6, pb_7, pr_1, pr_2, prb_3, prb_4, prb_5, prb_6, prb_7)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_65537_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng8n = range(51200, 65536)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6]; p_6 = Pxx[rng6]
    f_7 = freq[rng7]; p_7 = Pxx[rng7]
    f_8 = freq[rng8n]; p_8 = Pxx[rng8n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:467]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                                        pb_7, pb_8), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512+1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_LOWFMIC_' in x_n or '_TEMPERATURE_' in x_n:
        rng_lowfmictemp = range(16, 154)
        p_lowfmictemp = Pxx[rng_lowfmictemp]
        if np.sqrt(sum(p_lowfmictemp) * 1/512) < \
           disconnect_lowfmictemperature_th \
           and np.amin(np.sqrt(p_lowfmictemp)) > \
           comb_lowfmictemperature_th * 0.1:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        comb_amp = np.sqrt(p_lowfmictemp)
        comb_num = sum(j < comb_lowfmictemperature_th for j in comb_amp)
        if comb_num > 5:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_TILT_' in x_n:
        rng_tilt = range(16, 512)
        p_tilt = Pxx[rng_tilt]
        if np.sqrt(sum(p_tilt) * 1/512) < disconnect_tilt_th \
           and np.amin(np.sqrt(p_tilt)) > comb_tilt_th * 0.1:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        comb_amp = np.sqrt(p_tilt)
        comb_num = sum(j < comb_tilt_th for j in comb_amp)
        if comb_num > 5:
            comb = 'Yes'
        else:
            comb = 'No'

    # Special case for 256hz incorrect LHO MAINSMON
    elif '_MAINSMON_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_80 = range(61*512, 80*512 + 1)
        rng10_80 = rng10_59 + rng61_80
        p10_80 = Pxx[rng10_80]
        rng59_61 = range(30464,30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.sqrt(sum(p10_80) * 1/512) < disconnect_128hzmainsmon_th \
           and np.amin(np.sqrt(p10_80)) > comb_th and np.amax(p59_61) \
           < mainsmonat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_80)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng1_59 = range(512, 59*512 + 1)
        rng61_80 = range(61* 512,80*512 + 1)
        rng1_80 = rng1_59 + rng61_80
        p1_80 = Pxx[rng1_80]
        if np.sqrt(sum(p1_80) * 1/512) < disconnect_65537_case_th \
           and np.amin(np.sqrt(p1_80)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p1_80)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_65537_and_131073_case(run_dir, x_n, x_nn, strcurGpsTime, \
             strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, p_1, \
             p_2, p_3, p_4, p_5, p_6, p_7, p_8, fb_3, fb_4, fb_5, fb_6, fb_7, \
             fb_8, pb_3, pb_4, pb_5, pb_6, pb_7, pb_8, pr_1, pr_2, prb_3, \
             prb_4, prb_5, prb_6, prb_7, prb_8)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_131073_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng8n = range(51200, 131072)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6]; p_6 = Pxx[rng6]
    f_7 = freq[rng7]; p_7 = Pxx[rng7]
    f_8 = freq[rng8n]; p_8 = Pxx[rng8n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:532]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                                        pb_7, pb_8), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = 0
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_65537_and_131073_case(run_dir, x_n, x_nn, strcurGpsTime, \
             strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, p_1, \
             p_2, p_3, p_4, p_5, p_6, p_7, p_8, fb_3, fb_4, fb_5, fb_6, fb_7, \
             fb_8, pb_3, pb_4, pb_5, pb_6, pb_7, pb_8, pr_1, pr_2, prb_3, \
             prb_4, prb_5, prb_6, prb_7, prb_8)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_262145_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                  data, Fs, freq, Pxx, Pxx_r):
    rng9n = range(153600, 262144)
    f_1 = freq[rng1]; p_1 = Pxx[rng1]
    f_2 = freq[rng2]; p_2 = Pxx[rng2]
    f_3 = freq[rng3]; p_3 = Pxx[rng3]
    f_4 = freq[rng4]; p_4 = Pxx[rng4]
    f_5 = freq[rng5]; p_5 = Pxx[rng5]
    f_6 = freq[rng6]; p_6 = Pxx[rng6]
    f_7 = freq[rng7]; p_7 = Pxx[rng7]
    f_8 = freq[rng8]; p_8 = Pxx[rng8]
    f_9 = freq[rng9n]; p_9 = Pxx[rng9n]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:566]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                                    pb_7, pb_8, pb_9), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512+1) + \
                    range(121*512, 179*512 + 1) + range(181*512, 239*512 + 1) +\
                                                    range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
           and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    # Mar 31, 2015 LHO made this choice.
    elif '_MAINSMON_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_magmainsmon_th \
           and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) \
           < mainsmonat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100)*1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = 0
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_262145_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
             f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, p_1, p_2, p_3, p_4, \
             p_5, p_6, p_7, p_8, p_9, fb_3, fb_4, fb_5, fb_6, fb_7, fb_8, \
             fb_9, pb_3, pb_4, pb_5, pb_6, pb_7, pb_8, pb_9, pr_1, pr_2, \
             prb_3, prb_4, prb_5, prb_6, prb_7, prb_8, prb_9)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_524289_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                 data, Fs, freq, Pxx, Pxx_r):
    rng10n = range(512000, 524288)
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

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]
    prb_10 = Pxx_r[591:593]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)
    fb_10, pb_10 = get_binned_data(f_10, p_10, 10000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                             pb_7, pb_8, pb_9, pb_10), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512 + 1) + \
                   range(121*512, 179*512 + 1) + range(181*512, 239*512 + 1) + \
                                                range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
            and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    # Suppose to be this one
    elif '_MAINSMON_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_magmainsmon_th \
           and np.amin(np.sqrt(p10_100)) > comb_th and np.amax(p59_61) \
           < mainsmonat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = np.sqrt(sum(pb_10)) / np.sqrt(sum(prb_10))
    pc_11 = 0

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_524289_and_1048577_case(run_dir, x_n, x_nn, strcurGpsTime, \
             strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, \
             f_10, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, fb_3, \
             fb_4, fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, pb_3, pb_4, pb_5, \
             pb_6, pb_7, pb_8, pb_9, pb_10, pr_1, pr_2, prb_3, prb_4, prb_5, \
             prb_6, prb_7, prb_8, prb_9, prb_10)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_1048577_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                 data, Fs, freq, Pxx, Pxx_r):
    rng10n = range(512000, 1048576)
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

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]
    prb_10 = Pxx_r[591:645]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)
    fb_10, pb_10 = get_binned_data(f_10, p_10, 10000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                            pb_7, pb_8, pb_9, pb_10), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512 + 1) + \
                   range(121*512, 179*512 + 1) + range(181*512, 239*512 +1 ) + \
                    range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
           and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-CS_MAG_LVEA_INPUTOPTICS_Y_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-EX_MAG_VEA_FLOOR_X_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-EX_MAG_VEA_FLOOR_Y_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_MAG_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512,100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = np.sqrt(sum(pb_10)) / np.sqrt(sum(prb_10))
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
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_524289_and_1048577_case(run_dir, x_n, x_nn, strcurGpsTime, \
            strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, \
            f_10, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, fb_3, \
            fb_4, fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, pb_3, pb_4, pb_5, pb_6, \
            pb_7, pb_8, pb_9, pb_10, pr_1, pr_2, prb_3, prb_4, prb_5, prb_6, \
            prb_7, prb_8, prb_9, prb_10)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_2097153_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                  data, Fs, freq, Pxx, Pxx_r):
    rng11n = range(1536000, 2097152)
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

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]
    prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:700]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)
    fb_10, pb_10 = get_binned_data(f_10, p_10, 10000)
    fb_11, pb_11 = get_binned_data(f_11, p_11, 100000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                      pb_7, pb_8, pb_9, pb_10, pb_11), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512 + 1) + \
                   range(121*512, 179*512 + 1) + range(181*512, 239*512 + 1) + \
                   range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
           and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-CS_MAG_LVEA_INPUTOPTICS_Y_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-EX_MAG_VEA_FLOOR_X_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '-EX_MAG_VEA_FLOOR_Y_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magexcasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_MAG_' in x_n:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512,100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        rng59_61 = range(30464, 30976)
        p59_61 = np.sqrt(Pxx[rng59_61])
        if np.amin(np.sqrt(p10_100)) > comb_th \
           and np.amax(p59_61) < magasdat60hz:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100)*1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = np.sqrt(sum(pb_10)) / np.sqrt(sum(prb_10))
    pc_11 = np.sqrt(sum(pb_11)) / np.sqrt(sum(prb_11))

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_2097153_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
            f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11, p_1, p_2, \
            p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, fb_3, fb_4, fb_5, \
            fb_6, fb_7, fb_8, fb_9, fb_10, fb_11, pb_3, pb_4, pb_5, pb_6, \
            pb_7, pb_8, pb_9, pb_10, pb_11, pr_1, pr_2, prb_3, prb_4, prb_5, \
            prb_6, prb_7, prb_8, prb_9, prb_10, prb_11)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_for_4194305_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                                data, Fs, freq, Pxx, Pxx_r):
    rng11n = range(1536000, 4194304)
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
    rng11a = range(3000*512, 4000*512)
    rng11b = range(4000*512, 5000*512)
    rng11c = range(5000*512, 6000*512)
    rng11d = range(6000*512, 7000*512)
    rng11e = range(7000*512, 8192*512)
    f_11a = freq[rng11a]; p_11a = Pxx[rng11a]
    f_11b = freq[rng11b]; p_11b = Pxx[rng11b]
    f_11c = freq[rng11c]; p_11c = Pxx[rng11c]
    f_11d = freq[rng11d]; p_11d = Pxx[rng11d]
    f_11e = freq[rng11e]; p_11e = Pxx[rng11e]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]
    prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:721]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)
    fb_10, pb_10 = get_binned_data(f_10, p_10, 10000)
    fb_11, pb_11 = get_binned_data(f_11, p_11, 100000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                     pb_7, pb_8, pb_9, pb_10, pb_11), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512 + 1) + \
                   range(121*512, 179*512 + 1) + range(181*512, 239*512 + 1) + \
                   range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
           and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if  disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if  comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = np.sqrt(sum(pb_10)) / np.sqrt(sum(prb_10))
    pc_11 = np.sqrt(sum(pb_11)) / np.sqrt(sum(prb_11))

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_4194305_and_allother_case(run_dir, x_n, x_nn, strcurGpsTime, \
             strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, \
             f_10, f_11a, f_11b, f_11c, f_11d, f_11e, p_1, p_2, p_3, p_4, p_5, \
             p_6, p_7, p_8, p_9, p_10, p_11a, p_11b, p_11c, p_11d, p_11e, \
             fb_3, fb_4, fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, fb_11, pb_3, \
             pb_4, pb_5, pb_6, pb_7, pb_8, pb_9, pb_10, pb_11, pr_1, pr_2, \
             prb_3, prb_4, prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour

def do_all_other_case(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                                            data, Fs, freq, Pxx, Pxx_r):
    rng11n = range(1536000, 5120000)
    #Note: 16384Hz channels will be cut at 10,000Hz!
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
    rng11a = range(3000*512, 4000*512)
    rng11b = range(4000*512, 5000*512)
    rng11c = range(5000*512, 6000*512)
    rng11d = range(6000*512, 7000*512)
    rng11e = range(7000*512, 10000*512)
    f_11a = freq[rng11a]; p_11a = Pxx[rng11a]
    f_11b = freq[rng11b]; p_11b = Pxx[rng11b]
    f_11c = freq[rng11c]; p_11c = Pxx[rng11c]
    f_11d = freq[rng11d]; p_11d = Pxx[rng11d]
    f_11e = freq[rng11e]; p_11e = Pxx[rng11e]

    pr_1 = Pxx_r[0:36]; pr_2 = Pxx_r[36:138]; prb_3 = Pxx_r[138:174]
    prb_4 = Pxx_r[174:277]; prb_5 = Pxx_r[277:313]; prb_6 = Pxx_r[313:416]
    prb_7 = Pxx_r[416:452]; prb_8 = Pxx_r[452:555]; prb_9 = Pxx_r[555:591]
    prb_10 = Pxx_r[591:694]; prb_11 = Pxx_r[694:730]

    fb_3, pb_3 = get_binned_data(f_3, p_3, 10)
    fb_4, pb_4 = get_binned_data(f_4, p_4, 10)
    fb_5, pb_5 = get_binned_data(f_5, p_5, 100)
    fb_6, pb_6 = get_binned_data(f_6, p_6, 100)
    fb_7, pb_7 = get_binned_data(f_7, p_7, 1000)
    fb_8, pb_8 = get_binned_data(f_8, p_8, 1000)
    fb_9, pb_9 = get_binned_data(f_9, p_9, 10000)
    fb_10, pb_10 = get_binned_data(f_10, p_10, 10000)
    fb_11, pb_11 = get_binned_data(f_11, p_11, 100000)

    p_1_new = p_1.reshape((-1, 36))
    p_2_new = p_2.reshape((-1, 102))
    pb_new = np.concatenate((p_1_new[0], p_2_new[0], pb_3, pb_4, pb_5, pb_6, \
                                    pb_7, pb_8, pb_9, pb_10, pb_11), axis=0)
    Pxx_r_new = Pxx_r + alpha * (pb_new - Pxx_r)

    if '_SEIS_' in x_n:
        rng_seis = range(3*512, 30*512 + 1)
        p_seis = Pxx[rng_seis]
        if np.sqrt(sum(p_seis) * 1/512) < disconnect_seis_th \
           and np.amin(np.sqrt(p_seis)) > comb_seis_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p_seis)) < comb_seis_th:
            comb = 'Yes'
        else:
            comb = 'No'

    elif '_ACC_' in x_n or '_MIC_' in x_n:
        rng10_300 = range(10*512, 59*512 + 1) + range(61*512, 119*512 + 1) + \
                   range(121*512, 179*512 + 1) + range(181*512, 239*512 + 1) + \
                   range(241*512, 299*512 + 1)
        p10_300 = Pxx[rng10_300]
        if np.sqrt(sum(p10_300) * 1/512) < disconnect_accmic_th \
           and np.amin(np.sqrt(p10_300)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_300)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'
    else:
        rng10_59 = range(10*512, 59*512 + 1)
        rng61_100 = range(61*512, 100*512 + 1)
        rng10_100 = rng10_59 + rng61_100
        p10_100 = Pxx[rng10_100]
        if np.sqrt(sum(p10_100) * 1/512) < disconnect_th \
           and np.amin(np.sqrt(p10_100)) > comb_th:
            disconnect = 'Yes'
        else:
            disconnect = 'No'
        if np.amin(np.sqrt(p10_100)) < comb_th:
            comb = 'Yes'
        else:
            comb = 'No'

    if disconnect == 'Yes':
        disconhour = get_disconnected_yes_hour(run_dir, x_n)
    else:
        disconhour = 0
    if comb == 'Yes':
        daqfailhour = get_daqfailure_yes_hour(run_dir, x_n)
    else:
        daqfailhour = 0

    pc_1 = np.sqrt(sum(p_1)) / np.sqrt(sum(pr_1))
    pc_2 = np.sqrt(sum(p_2)) / np.sqrt(sum(pr_2))
    pc_3 = np.sqrt(sum(pb_3)) / np.sqrt(sum(prb_3))
    pc_4 = np.sqrt(sum(pb_4)) / np.sqrt(sum(prb_4))
    pc_5 = np.sqrt(sum(pb_5)) / np.sqrt(sum(prb_5))
    pc_6 = np.sqrt(sum(pb_6)) / np.sqrt(sum(prb_6))
    pc_7 = np.sqrt(sum(pb_7)) / np.sqrt(sum(prb_7))
    pc_8 = np.sqrt(sum(pb_8)) / np.sqrt(sum(prb_8))
    pc_9 = np.sqrt(sum(pb_9)) / np.sqrt(sum(prb_9))
    pc_10 = np.sqrt(sum(pb_10)) / np.sqrt(sum(prb_10))
    pc_11 = np.sqrt(sum(pb_11)) / np.sqrt(sum(prb_11))

    if '_SEIS_' in x_n:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    elif '_ACC_' in x_n or '_MIC_' in x_n:
        pc_list_2 = [pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'
    else:
        pc_list_1 = [pc_1, pc_2, pc_3]
        pc_list_2 = [pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11]
        cond_1 = [x for x in pc_list_1 if x > thd1g or x < thd1l and x > 0]
        cond_2 = [x for x in pc_list_2 if x > thd2g or x < thd2l and x > 0]
        if not cond_1 and not cond_2:
            excess = 'No'
        else:
            excess = 'Yes'

    if comb == 'Yes' or disconnect == 'Yes':
        status = 'Alert'
    else:
        status = 'Ok'

    pltutils.timeseries_plot(run_dir, x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs)
    pltutils.psdplot_4194305_and_allother_case(run_dir, x_n, x_nn, strcurGpsTime, \
             strcurUtcTime, Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, \
             f_10, f_11a, f_11b, f_11c, f_11d, f_11e, p_1, p_2, p_3, p_4, p_5, \
             p_6, p_7, p_8, p_9, p_10, p_11a, p_11b, p_11c, p_11d, p_11e, \
             fb_3, fb_4, fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, fb_11, pb_3, \
             pb_4, pb_5, pb_6, pb_7, pb_8, pb_9, pb_10, pb_11, pr_1, pr_2, \
             prb_3, prb_4, prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11)

    if status == 'Ok':
        newreffile = open(run_dir + '/ref_files/' + x_nn + '.txt', 'w')
        for item in Pxx_r_new:
            print >> newreffile, item
        newreffile.close()
    else:
        print 'Not saving spectra'

    return pc_1, pc_2, pc_3, pc_4, pc_5, pc_6, pc_7, pc_8, pc_9, pc_10, pc_11, \
           excess, comb, disconnect, status, disconhour, daqfailhour
