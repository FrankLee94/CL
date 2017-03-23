#!usr/bin/env python
#-*- coding:utf-8 -*-

# this model is for different traffic graph
# JialongLi 2016/12/15

import string
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

def graph():
	traffic_0 = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.40, 0.60, 1.00, 1.00, 1.00, 1.00, 1.00, \
	1.00, 1.00, 1.00, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40]
	for i in range(24):
		traffic_0[i] = traffic_0[i] * 64

	traffic_1 = [13.40, 13.54, 14.23, 12.45, 14.85, 13.91, 21.28, 39.7, 61.23, 53.79, 63.32, 68.65, \
	63.81, 51.95, 58.64, 56.6, 30.79, 24.54, 24.36, 25.83, 30.48, 21.42, 27.16, 28.98]
	traffic_2 = [12.18, 9.10, 10.08, 15.52, 13.31, 14.84, 26.54, 45.53, 81.59, 68.64, 72.11, 54.76, \
	66.93, 68.98, 49.56, 55.89, 26.29, 27.09, 24.37, 26.11, 24.18, 25.82, 27.79, 21.16]
	traffic_3 = [12.38, 13.62, 14.89, 17.32, 17.06, 13.81, 31.8, 40.44, 46.82, 89.06, 71.48, 62.01, \
	39.89, 83.69, 61.85, 41.75, 32.08, 28.93, 36.1, 22.3, 30.36, 30.17, 22.04, 16.77]

	for i in range(24):
		traffic_0[i] = traffic_0[i] / 100;
		traffic_1[i] = traffic_1[i] / 100;
		traffic_2[i] = traffic_2[i] / 100;
		traffic_3[i] = traffic_3[i] / 100;

	bar_width = 0.5
	opacity = 0.4
	index = range(1, 25)

	p1 = plt.subplot(221)
	rects1 = p1.bar(index, traffic_0, bar_width, alpha = opacity, color='blue')
	ind = np.linspace(4, 24, 6)
	p1.set_xticks(ind + bar_width / 2)  
	p1.set_xticklabels(['4:00', '8:00', '12:00', '16:00', '20:00', '24:00'], fontsize = 10)
	p1.set_title('basic traffic (variance = $ \sigma_{0}^{2} $)', fontsize = 12)
	p1.set_ylabel('normalized total traffic load', fontsize = 10)
	plt.yticks(fontsize = 8)
	plt.ylim(0, 1)

	opacity = 0.4
	index = range(1, 25)
	p2 = plt.subplot(222)
	rects2 = p2.bar(index, traffic_1, bar_width, alpha = opacity, color='blue')
	#rects2 = p2.bar(index, traffic_0, bar_width, alpha = opacity, hatch = '//', color='blue')
	ind = np.linspace(4, 24, 6)
	p2.set_xticks(ind + bar_width / 2)
	p2.set_xticklabels(['4:00', '8:00', '12:00', '16:00', '20:00', '24:00'], fontsize = 10)
	p2.set_title('traffic-I (variance = $ 1.06\sigma_{0}^{2} $)', fontsize = 12)
	p2.set_ylabel('normalized total traffic load', fontsize = 10)
	plt.yticks(fontsize = 8)
	plt.ylim(0, 1)

	opacity = 0.4
	index = range(1, 25)
	p3 = plt.subplot(223)
	rects3 = p3.bar(index, traffic_2, bar_width, alpha = opacity, color='blue')
	#rects3 = p3.bar(index, traffic_0, bar_width, alpha = opacity, hatch = '//', color='None')
	ind = np.linspace(4, 24, 6)
	p3.set_xticks(ind + bar_width / 2)  
	p3.set_xticklabels(['4:00', '8:00', '12:00', '16:00', '20:00', '24:00'], fontsize = 10)
	p3.set_title('traffic-II (variance = $ 1.11\sigma_{0}^{2} $)', fontsize = 12)
	p3.set_ylabel('normalized total traffic load', fontsize = 10)
	plt.yticks(fontsize = 8)
	plt.ylim(0, 1)


	opacity = 0.4
	index = range(1, 25)
	p4 = plt.subplot(224)
	rects4 = p4.bar(index, traffic_3, bar_width, alpha = opacity, color='blue')
	#rects4 = p4.bar(index, traffic_0, bar_width, alpha = opacity,  color='blue')
	ind = np.linspace(4, 24, 6)
	p4.set_xticks(ind + bar_width / 2)  
	p4.set_xticklabels(['4:00', '8:00', '12:00', '16:00', '20:00', '24:00'], fontsize = 10)
	p4.set_title('traffic-III (variance = $ 1.20\sigma_{0}^{2} $)', fontsize = 12)
	p4.set_ylabel('normalized total traffic load', fontsize = 10)
	plt.yticks(fontsize = 8)
	plt.ylim(0, 1)


	plt.show()
if __name__ == '__main__':
	graph()
