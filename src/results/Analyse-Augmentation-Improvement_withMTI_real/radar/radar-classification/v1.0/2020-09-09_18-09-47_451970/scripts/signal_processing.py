from pyemd import emd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
#
# def eClean_algorithm(iq_mat):
#     #Calculate histogram
#     histogram, bin_edges = np.histogram(iq_mat, bins=32*126, range=(np.min(iq_mat), np.max(iq_mat)))
#     histogram, bin_edges = np.histogram(iq[0], bins=32*126, range=(np.min(iq[0]), np.max(iq[0])))
#     plt.figure()
#     plt.plot(np.linspace(np.min(iq[0]), np.max(iq[0],int(histogram.shape[0])), histogram, linewidth=2)
#     plt.savefig(os.getcwd() + 'histogram')
#     secound_derviative = np.diff(histogram,n=2)
#     plt.figure()
#     plt.plot(np.linspace(np.min(secound_derviative[0]), np.max(secound_derviative[0], int(secound_derviative.shape[0])), secound_derviative, linewidth=2)
#     plt.savefig(os.getcwd() + 'secound_derviative')
#     threshold = 3
#     index = np.where((secound_derviative / secound_derviative[1]) < threshold)  # results in 3
#
# # def pre_process_signal(iq_mat):

def EMD_Transformation(iq_mat):
    emd_inst = emd()
    IMFs = emd_inst(iq_mat)
    # TODO: analyse what are the actual relevant IMFs and remove the redundant indices
    plot_results(IMFs)
    new_iq_mat = sum(IMFs)
    return new_iq_mat

def plot_results(IMFs):
    plt.figure(figsize=(16, 8))
    plt.plot(range(IMFs[0]), IMFs[0], '0')
    plt.grid(True)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (secs)')
    plt.show()
    plt.figure(figsize=(16, 8))
    plt.grid(True)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (secs)')
    plt.show()
    plt.plot(range(IMFs[1]), IMFs[1], '1')
    plt.figure(figsize=(16, 8))
    plt.grid(True)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (secs)')
    plt.show()
    plt.plot(range(IMFs[2]), IMFs[2], '2')
    plt.grid(True)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (secs)')
    plt.show()
    plt.figure(figsize=(16, 8))
    plt.plot(range(IMFs[3]), IMFs[3], '3')
    plt.grid(True)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (secs)')
    plt.show()