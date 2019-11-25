from development.log_manager import read_log
from development.eval_methods import calculate_stats

import matplotlib.pyplot as plt
import time
import numpy as np

if __name__ == '__main__':

    while True:

        detected_object_list = read_log('../output/detection_log.txt')
        precisions = np.zeros(((len(detected_object_list)-2),), dtype='float32')
        recalls = np.zeros(((len(detected_object_list)-2),), dtype='float32')

        for i in range(1, len(detected_object_list)-1):
            precision1, recall1 = calculate_stats(detected_object_list[i-1], detected_object_list[i])
            precision2, recall2 = calculate_stats(detected_object_list[i], detected_object_list[i+1])
            precisions[i-1] = max(precision1, precision2)
            recalls[i-1] = max(recall1, recall2)

        plt.clf()
        plt.plot(precisions)
        plt.plot(recalls)
        plt.plot()
        plt.ylim([0, 1.1])
        plt.legend(['precision', 'recall'])
        plt.pause(0.5)






