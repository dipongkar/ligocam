import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pylab as plb
import numpy as np

run_dir = '/home/dtalukder/Projects/detchar/LigoCAM/PEM/'

def timeseries_plot(x_n, x_nn, strcurGpsTime, strcurUtcTime, data, Fs):
    dlen = int(len(data) / 512)
    fig = plt.figure(2, figsize=(10,8))
    plt.subplot(311)
    plt.plot(range(0, 50*dlen), data[range(0, 50*dlen)], 'green', \
    range(50*dlen, 100*dlen), data[range(50*dlen, 100*dlen)], 'green', \
    range(100*dlen, 150*dlen), data[range(100*dlen, 150*dlen)], 'green', \
    range(150*dlen, 200*dlen), data[range(150*dlen, 200*dlen)], 'green', \
    range(200*dlen, 250*dlen), data[range(200*dlen, 250*dlen)], 'green', \
    range(250*dlen, 300*dlen), data[range(250*dlen, 300*dlen)], 'green', \
    range(300*dlen, 350*dlen), data[range(300*dlen, 350*dlen)], 'green', \
    range(350*dlen, 400*dlen), data[range(350*dlen, 400*dlen)], 'green', \
    range(400*dlen, 450*dlen), data[range(400*dlen, 450*dlen)], 'green', \
    range(450*dlen, 512*dlen), data[range(450*dlen, 512*dlen)], 'green')
    plb.xlim([0, len(data)])
    plt.grid(True)
    plb.xticks([0, 100*Fs, 200*Fs, 300*Fs, 400*Fs, 500*Fs], \
                      ['0', '100', '200', '300', '400', '500'])
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.plot(data[range(0, dlen)], 'green')
    plb.xlim([0, dlen+50])
    plt.grid(True)
    plb.xticks([0, (dlen-1)/2, dlen-1], ['0', '0.5', '1'])
    plt.ylabel('Amplitude [counts]', fontsize=14)
    plt.subplot(313)
    plt.plot(data[range(511*dlen-1, 512*dlen)], 'green')
    plb.xlim([-50, dlen])
    plb.xticks([0, (dlen-1)/2, dlen-1], ['511', '511.5', '512'])
    plt.xlabel('Time [s]', fontsize=14)
    plt.grid(True)
    fig.savefig(run_dir + 'images/TS/' + strcurGpsTime + '/' + x_nn + \
                                                        '.png', dpi=75)
    fig.clf()

def psdplot_4097_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, f_1, f_2, \
                     f_3, f_4, f_5, p_1, p_2, p_3, p_4, p_5, fb_3, fb_4, fb_5, \
                     pb_3, pb_4, pb_5, pr_1, pr_2, prb_3, prb_4, prb_5):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1, np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
              axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
              axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
              np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
              np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                              fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(f_5, np.sqrt(p_5), 'LightBlue', fb_5, np.sqrt(prb_5), 'red',
                                              fb_5, np.sqrt(pb_5), 'blue')
    plb.xlim([f_5.min(), 300])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(1, 1, 'w', 1, 1, 'w')
    plb.xlim([300, 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plb.yticks([], [])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_8193_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, f_1, f_2, \
                     f_3, f_4, f_5, f_6, p_1, p_2, p_3, p_4, p_5, p_6, fb_3, \
                     fb_4, fb_5, fb_6, pb_3, pb_4, pb_5, pb_6, pr_1, pr_2, \
                     prb_3, prb_4, prb_5, prb_6):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1, np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
              axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
              axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
              np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
              np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                            fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6), axis=1), \
               np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0])), \
               axis=1), 'LightBlue', np.concatenate((fb_5, fb_6), axis=1), \
               np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6)), axis=1), \
               'red', np.concatenate((fb_5, fb_6), axis=1), \
               np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6)), axis=1), 'blue')
    plb.xlim([f_5.min(), 300])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(1, 1, 'w', 1, 1, 'w')
    plb.xlim([300, 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plb.yticks([], [])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_Dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_16385_and_32769_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
                      f_1, f_2, f_3, f_4, f_5, f_6, f_7, p_1, p_2, p_3, p_4, \
                      p_5, p_6, p_7, fb_3, fb_4, fb_5, fb_6, fb_7, pb_3, pb_4, \
                      pb_5, pb_6, pb_7, pr_1, pr_2, prb_3, prb_4, prb_5, \
                      prb_6, prb_7):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1, np.sqrt(p_1), 'blue', \
                np.concatenate((f_3, f_4), axis=1), \
                np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
                axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
                axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
                np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
                np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
                np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
                np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                              fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7), axis=1), \
               np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
               np.sqrt(p_7[:, 0])), axis=1), 'LightBlue', \
               np.concatenate((fb_5, fb_6, fb_7), axis=1), \
               np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), \
               np.sqrt(prb_7)), axis=1), 'red', \
               np.concatenate((fb_5, fb_6, fb_7), axis=1), \
               np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7)), \
               axis=1), 'blue')
    plb.xlim([f_5.min(), 300])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(1, 1, 'w', 1, 1, 'w')
    plb.xlim([300, 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plb.yticks([], [])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_65537_and_131073_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, \
                  f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, p_1, p_2, p_3, p_4, \
                  p_5, p_6, p_7, p_8, fb_3, fb_4, fb_5, fb_6, fb_7, fb_8, \
                  pb_3, pb_4, pb_5, pb_6, pb_7, pb_8, pr_1, pr_2, prb_3, \
                  prb_4, prb_5, prb_6, prb_7, prb_8):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1, np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), axis=1), \
              'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), np.sqrt(prb_3), \
              np.sqrt(prb_4)), axis=1), 'red', \
              np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)) ,axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                            fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7, f_8), axis=1), \
              np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
              np.sqrt(p_7[:, 0]), np.sqrt(p_8[:, 0])), axis=1), 'LightBlue', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), np.sqrt(prb_7), \
              np.sqrt(prb_8)), axis=1), 'red', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7), \
              np.sqrt(pb_8)), axis=1), 'blue')
    plb.xlim([f_5.min(), 300])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(1, 1, 'w', 1, 1, 'w')
    plb.xlim([300, 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plb.yticks([], [])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_262145_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, f_1, f_2, \
                   f_3, f_4, f_5, f_6, f_7, f_8, f_9, p_1, p_2, p_3, p_4, p_5, \
                   p_6, p_7, p_8, p_9, fb_3, fb_4, fb_5, fb_6, fb_7, fb_8, \
                   fb_9, pb_3, pb_4, pb_5, pb_6, pb_7, pb_8, pb_9, pr_1, pr_2, \
                   prb_3, prb_4, prb_5, prb_6, prb_7, prb_8, prb_9):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1, np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
              axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
              axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
              np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
              np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                              fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7, f_8), axis=1), \
              np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
              np.sqrt(p_7[: ,0]), np.sqrt(p_8[:, 0])), axis=1), 'LightBlue', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), np.sqrt(prb_7), \
              np.sqrt(prb_8)), axis=1), 'red', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7), \
              np.sqrt(pb_8)), axis=1), 'blue')
    plb.xlim([f_5.min(), f_8.max()])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(f_9, np.sqrt(p_9), 'LightBlue', fb_9, np.sqrt(prb_9), 'red', \
                                                 fb_9, np.sqrt(pb_9), 'blue')
    plb.xlim([f_9.min(), 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_524289_and_1048577_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, \
                Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, p_1, \
                p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, fb_3, fb_4, \
                fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, pb_3, pb_4, pb_5, pb_6, \
                pb_7, pb_8, pb_9, pb_10, pr_1, pr_2, prb_3, prb_4, prb_5, \
                prb_6, prb_7, prb_8, prb_9, prb_10):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1,np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
              axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
              axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
              np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), \
              'red', np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                             fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7, f_8), axis=1), \
              np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
              np.sqrt(p_7[:, 0]), np.sqrt(p_8[:, 0])), axis=1), 'LightBlue', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), np.sqrt(prb_7), \
              np.sqrt(prb_8)), axis=1), 'red', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7), \
              np.sqrt(pb_8)), axis=1), 'blue')
    plb.xlim([f_5.min(), f_8.max()])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(f_9, np.sqrt(p_9), 'LightBlue', f_10, np.sqrt(p_10), \
               'LightBlue', np.concatenate((fb_9, fb_10), axis=1), \
               np.concatenate((np.sqrt(prb_9), np.sqrt(prb_10)), axis=1), \
               'red', np.concatenate((fb_9, fb_10), axis=1), \
               np.concatenate((np.sqrt(pb_9), np.sqrt(pb_10)), axis=1), 'blue')
    plb.xlim([f_9.min(), 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_2097153_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, Fs, f_1, \
                   f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11, p_1, \
                   p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, fb_3, \
                   fb_4, fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, fb_11, pb_3, \
                   pb_4, pb_5, pb_6, pb_7, pb_8, pb_9, pb_10, pb_11, pr_1, \
                   pr_2, prb_3, prb_4, prb_5, prb_6, prb_7, prb_8, prb_9, \
                   prb_10, prb_11):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1,np.sqrt(p_1), 'blue', \
              np.concatenate((f_3, f_4), axis=1), \
              np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
              axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
              axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
              np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
              np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
              np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
              np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                              fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7, f_8), axis=1), \
              np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
              np.sqrt(p_7[:, 0]), np.sqrt(p_8[:, 0])), axis=1), 'LightBlue', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), np.sqrt(prb_7), \
              np.sqrt(prb_8)), axis=1), 'red', \
              np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
              np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7), \
              np.sqrt(pb_8)), axis=1), 'blue')
    plb.xlim([f_5.min(), f_8.max()])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(f_9, np.sqrt(p_9), 'LightBlue', f_10, np.sqrt(p_10), \
              'LightBlue', f_11, np.sqrt(p_11), 'LightBlue', \
              np.concatenate((fb_9, fb_10, fb_11), axis=1), \
              np.concatenate((np.sqrt(prb_9), np.sqrt(prb_10), \
              np.sqrt(prb_11)), axis=1), 'red', \
              np.concatenate((fb_9, fb_10, fb_11), axis=1), \
              np.concatenate((np.sqrt(pb_9), np.sqrt(pb_10), np.sqrt(pb_11)), \
              axis=1), 'blue')
    plb.xlim([f_9.min(), 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()

def psdplot_4194305_and_allother_case(x_n, x_nn, strcurGpsTime, strcurUtcTime, \
            Fs, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11a, \
            f_11b, f_11c, f_11d, f_11e, p_1, p_2, p_3, p_4, p_5, p_6, p_7, \
            p_8, p_9, p_10, p_11a, p_11b, p_11c, p_11d, p_11e, fb_3, fb_4, \
            fb_5, fb_6, fb_7, fb_8, fb_9, fb_10, fb_11, pb_3, pb_4, pb_5, \
            pb_6, pb_7, pb_8, pb_9, pb_10, pb_11, pr_1, pr_2, prb_3, prb_4, \
            prb_5, prb_6, prb_7, prb_8, prb_9, prb_10, prb_11):
    fig = plt.figure(1, figsize=(10,8))
    plt.subplot(311)
    plt.loglog(f_1, np.sqrt(pr_1), 'red', f_1,np.sqrt(p_1), 'blue', \
               np.concatenate((f_3, f_4), axis=1), \
               np.concatenate((np.sqrt(p_3[:, 0]), np.sqrt(p_4[:, 0])), \
               axis=1), 'LightBlue', np.concatenate((f_1, f_2, fb_3, fb_4), \
               axis=1), np.concatenate((np.sqrt(pr_1), np.sqrt(pr_2), \
               np.sqrt(prb_3), np.sqrt(prb_4)), axis=1), 'red', \
               np.concatenate((f_1, f_2, fb_3, fb_4), axis=1), \
               np.concatenate((np.sqrt(p_1[:, 0]), np.sqrt(p_2[:, 0]), \
               np.sqrt(pb_3), np.sqrt(pb_4)), axis=1), 'blue')
    leg = plt.legend(('Reference', 'Current',), 'lower left', shadow=False, \
                                                              fancybox=False)
    leg.get_frame().set_alpha(0.5)
    plb.xlim([f_1.min(), f_4.max()])
    plb.xticks([0.03, 0.1, 0.3, 1, 3], ['0.03', '0.1', '0.3', '1', '3'])
    plt.grid(True)
    plt.title('Epoch: ' + strcurUtcTime + ', Channel: ' + x_n, fontsize=14)
    plt.subplot(312)
    plt.loglog(np.concatenate((f_5, f_6, f_7, f_8), axis=1), \
               np.concatenate((np.sqrt(p_5[:, 0]), np.sqrt(p_6[:, 0]), \
               np.sqrt(p_7[:, 0]), np.sqrt(p_8[:, 0])), axis=1), 'LightBlue', \
               np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
               np.concatenate((np.sqrt(prb_5), np.sqrt(prb_6), np.sqrt(prb_7), \
               np.sqrt(prb_8)), axis=1), 'red', \
               np.concatenate((fb_5, fb_6, fb_7, fb_8), axis=1), \
               np.concatenate((np.sqrt(pb_5), np.sqrt(pb_6), np.sqrt(pb_7), \
               np.sqrt(pb_8)), axis=1), 'blue')
    plb.xlim([f_5.min(), f_8.max()])
    plb.xticks([3, 10, 30, 100, 300], ['3', '10', '30', '100', '300'])
    plt.grid(True)
    plt.ylabel('Amplitude [counts/sqrt(Hz)]', fontsize=14)
    plt.subplot(313)
    plt.loglog(f_9, np.sqrt(p_9), 'LightBlue', f_10, np.sqrt(p_10), \
               'LightBlue', f_11a, np.sqrt(p_11a), 'LightBlue', f_11b, \
               np.sqrt(p_11b), 'LightBlue', f_11c, np.sqrt(p_11c), \
               'LightBlue', f_11d, np.sqrt(p_11d), 'LightBlue', f_11e, \
               np.sqrt(p_11e), 'LightBlue', \
               np.concatenate((fb_9, fb_10, fb_11), axis=1), \
               np.concatenate((np.sqrt(prb_9), np.sqrt(prb_10), \
               np.sqrt(prb_11)), axis=1), 'red', \
               np.concatenate((fb_9, fb_10, fb_11), axis=1), \
               np.concatenate((np.sqrt(pb_9), np.sqrt(pb_10), np.sqrt(pb_11)), \
               axis=1), 'blue')
    plb.xlim([f_9.min(), 10000])
    plb.xticks([300, 1000, 3000, 10000], ['300', '1000', '3000', '10000'])
    plt.grid(True)
    plt.xlabel('Frequency [Hz]', fontsize=14)
    fig.savefig(run_dir + 'images/ASD/' + strcurGpsTime + '/' + x_nn + '.png')
    fig.clf()
