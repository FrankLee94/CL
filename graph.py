#!usr/bin/env python
#-*- coding:utf-8 -*-

# this model is for depicting graph
# JialongLi 2016/12/07

import string
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from matplotlib.ticker import  MultipleLocator, FormatStrFormatter

def energy():
	period = [1, 2, 3, 4, 5, 6, 7]
	energy_0 = [1, 1, 1, 1, 1, 1, 1]
	energy_1 = [1.0235, 1.0313, 1.0341, 1.036, 1.03601, 1.0364, 1.0366]
	energy_2 = [1.0427, 1.0584, 1.0656, 1.0695, 1.0718, 1.0740, 1.0752]
	energy_3 = [1.0579, 1.0811, 1.0933, 1.0997, 1.1054, 1.1111, 1.1144]
	energy_4 = [1.0705, 1.1007, 1.1181, 1.1276, 1.1373, 1.1482, 1.1540]
	energy_5 = [1.0810, 1.1174, 1.1400, 1.1543, 1.1678, 1.1837, 1.1932]
	plt.plot(period, energy_0, color = 'red', linewidth = 2, marker = '*', markerfacecolor = 'red', markersize = 10, label = 'MES')
	plt.plot(period, energy_1, color = 'green', linewidth = 2, marker = 'D', markerfacecolor = 'green', markersize = 10, label = 'WPS-1')
	plt.plot(period, energy_2, color = 'blue', linewidth = 2, marker = 's', markerfacecolor = 'blue', markersize = 10, label = 'WPS-2')
	plt.plot(period, energy_3, color = 'cyan', linewidth = 2, marker = 'v', markerfacecolor = 'cyan', markersize = 10, label = 'WPS-3')
	plt.plot(period, energy_4, color = 'magenta', linewidth = 2, marker = 'p', markerfacecolor = 'magenta', markersize = 10, label = 'WPS-4')
	plt.plot(period, energy_5, color = 'yellow', linewidth = 2, marker = 'o', markerfacecolor = 'yellow', markersize = 10, label = 'WPS-5')
	plt.legend(loc = 'upper left', fontsize = 14)
	plt.ylim(0.98, 1.22)
	plt.xlim(1, 7)
	plt.xlabel('period(hour)', fontsize = 18)
	plt.ylabel('relative energy consumption', fontsize = 18)
	plt.grid(True)
	plt.show()

def lifetime():
	period = [1, 2, 3, 4, 5, 6, 7]
	lifetime_0 = [0.4424, 0.4424, 0.4424, 0.4424, 0.4424, 0.4424, 0.4424]
	lifetime_1 = [0.4658, 0.4754, 0.4780, 0.4800, 0.4802, 0.4806, 0.4808]
	lifetime_2 = [0.4828, 0.5009, 0.5074, 0.5115, 0.5122, 0.5151, 0.5168]
	lifetime_3 = [0.4952, 0.5197, 0.5298, 0.5350, 0.5354, 0.5433, 0.5471]
	lifetime_4 = [0.5050, 0.5342, 0.5476, 0.5529, 0.5526, 0.5667, 0.5740]
	lifetime_5 = [0.5125, 0.5458, 0.5608, 0.5671, 0.5674, 0.5824, 0.5975]
	plt.plot(period, lifetime_0, color = 'red', linewidth = 2, marker = '*', markerfacecolor = 'red', markersize = 10, label = 'MES')
	plt.plot(period, lifetime_1, color = 'green', linewidth = 2, marker = 'D', markerfacecolor = 'green', markersize = 10, label = 'WPS-1')
	plt.plot(period, lifetime_2, color = 'blue', linewidth = 2, marker = 's', markerfacecolor = 'blue', markersize = 10, label = 'WPS-2')
	plt.plot(period, lifetime_3, color = 'cyan', linewidth = 2, marker = 'v', markerfacecolor = 'cyan', markersize = 10, label = 'WPS-3')
	plt.plot(period, lifetime_4, color = 'magenta', linewidth = 2, marker = 'p', markerfacecolor = 'magenta', markersize = 10, label = 'WPS-4')
	plt.plot(period, lifetime_5, color = 'yellow', linewidth = 2, marker = 'o', markerfacecolor = 'yellow', markersize = 10, label = 'WPS-5')
	plt.legend(loc = 'upper left', fontsize = 14)
	plt.ylim(0.43, 0.62)
	plt.xlim(1, 7)
	plt.xlabel('period(hour)', fontsize = 18)
	plt.ylabel('normalized device lifetime', fontsize = 18)
	plt.grid(True)
	plt.show()

def migration():
	period = [1, 2, 3, 4, 5, 6, 7]
	lifetime_0 = [0.2135, 0.2135, 0.2135, 0.2135, 0.2135, 0.2135, 0.2135]
	lifetime_1 = [0.1620, 0.1479, 0.1446, 0.1429, 0.1428, 0.1424, 0.1425]
	lifetime_2 = [0.1496, 0.1295, 0.1245, 0.1220, 0.1219, 0.1201, 0.1195]
	lifetime_3 = [0.1445, 0.1225, 0.1156, 0.1136, 0.1136, 0.1100, 0.1084]
	lifetime_4 = [0.1422, 0.1187, 0.1101, 0.1085, 0.1084, 0.1027, 0.0998]
	lifetime_5 = [0.1410, 0.1171, 0.1069, 0.1049, 0.1044, 0.0982, 0.0923]
	plt.plot(period, lifetime_0, color = 'red', linewidth = 2, marker = '*', markerfacecolor = 'red', markersize = 10, label = 'MES')
	plt.plot(period, lifetime_1, color = 'green', linewidth = 2, marker = 'D', markerfacecolor = 'green', markersize = 10, label = 'WPS-1')
	plt.plot(period, lifetime_2, color = 'blue', linewidth = 2, marker = 's', markerfacecolor = 'blue', markersize = 10, label = 'WPS-2')
	plt.plot(period, lifetime_3, color = 'cyan', linewidth = 2, marker = 'v', markerfacecolor = 'cyan', markersize = 10, label = 'WPS-3')
	plt.plot(period, lifetime_4, color = 'magenta', linewidth = 2, marker = 'p', markerfacecolor = 'magenta', markersize = 10, label = 'WPS-4')
	plt.plot(period, lifetime_5, color = 'yellow', linewidth = 2, marker = 'o', markerfacecolor = 'yellow', markersize = 10, label = 'WPS-5')
	plt.legend(loc = 'upper left', fontsize = 14)  #bbox_to_anchor = (0, 0.5))
	plt.ylim(0.08, 0.23)
	plt.xlim(1, 7)
	plt.xlabel('period(hour)', fontsize = 18)
	plt.ylabel('normalized traffic migration', fontsize = 18)
	plt.grid(True)
	plt.show()

def pareto_lifetime():
	POINT_NUM = 15
	energy = []
	lifetime_de = []
	file_lifetime = open('./lifetime_energy.txt', 'r')
	for line_num in range(6):
		line = file_lifetime.readline().decode('utf-8')
		temp = [float(line.split()[i]) for i in range(POINT_NUM)]
		if line_num % 2 == 0:
			energy.append(temp)
		else:
			lifetime_de.append(temp)

	plt.plot(energy[0], lifetime_de[0], color = 'green', linewidth = 2, marker = 'o', markerfacecolor = 'green', markersize = 8, label = 'Traffic-I $\ $ = $ 1.06\sigma_{0}^{2} $')
	plt.plot(energy[1], lifetime_de[1], color = 'blue', linewidth = 2, marker = 'D', markerfacecolor = 'blue', markersize = 8, label = 'Traffic-II $\,$ = $ 1.11\sigma_{0}^{2} $')
	plt.plot(energy[2], lifetime_de[2], color = 'cyan', linewidth = 2, marker = 's', markerfacecolor = 'cyan', markersize = 8, label = 'Traffic-III  = $ 1.20\sigma_{0}^{2} $')
	plt.legend(loc = 'upper right')
	plt.ylim(0.27, 0.60)
	plt.xlim(1, 1.22)
	plt.xlabel('relative energy consumption', fontsize = 18)
	plt.ylabel('1 - normalized device lifetime', fontsize = 18)

	plt.annotate('', xy=(1, 0.4510), xytext=(1.028, 0.55), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1, 0.5091), xytext=(1.028, 0.55), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1, 0.5576), xytext=(1.028, 0.55), arrowprops=dict(arrowstyle="->"))
	plt.text(1.03, 0.55, 'default points', fontsize = 18)
	plt.annotate('', xy=(1.201, 0.2874), xytext=(1.16855, 0.45), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.201, 0.3440), xytext=(1.16855, 0.45), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.201, 0.4025), xytext=(1.16855, 0.45), arrowprops=dict(arrowstyle="->"))
	plt.text(1.136, 0.471, 'minimum lifetime', fontsize = 18)
	plt.text(1.130, 0.451, 'degeneration points', fontsize = 18)
	plt.grid(True)
	plt.show()

def pareto_migration():
	POINT_NUM = 15
	energy = []
	migration = []
	file_migration = open('./migration_energy.txt', 'r')
	for line_num in range(6):
		line = file_migration.readline().decode('utf-8')
		temp = [float(line.split()[i]) for i in range(POINT_NUM)]
		if line_num % 2 == 0:
			energy.append(temp)
		else:
			migration.append(temp)

	ax = plt.gca()
	ymajorLocator = MultipleLocator(0.02);
	ymajorFormatter = FormatStrFormatter('%1.2f') #设置y轴标签文本的格式  
	#yminorLocator   = MultipleLocator(0.02) #将此y轴次刻度标签设置为0.1的倍数
	#yminorFormatter = FormatStrFormatter('%1.1f') #设置y轴标签文本的格式 
	ax.yaxis.set_major_locator(ymajorLocator)  
	ax.yaxis.set_major_formatter(ymajorFormatter)  
	#ax.yaxis.set_minor_locator(yminorLocator)
	ax.yaxis.grid(True, which='major') #y坐标轴的网格使用次刻度  

	plt.plot(energy[0], migration[0], color = 'green', linewidth = 2, marker = 'o', markerfacecolor = 'green', markersize = 8, label = 'Traffic-I $\ $ = $ 1.06\sigma_{0}^{2} $')
	plt.plot(energy[1], migration[1], color = 'blue', linewidth = 2, marker = 'D', markerfacecolor = 'blue', markersize = 8, label = 'Traffic-II $\,$ = $ 1.11\sigma_{0}^{2} $')
	plt.plot(energy[2], migration[2], color = 'cyan', linewidth = 2, marker = 's', markerfacecolor = 'cyan', markersize = 8, label = 'Traffic-III  = $ 1.20\sigma_{0}^{2} $')
	plt.legend(loc = 'upper right')
	plt.ylim(0.05, 0.23)
	plt.xlim(1, 1.22)
	plt.xlabel('relative energy consumption', fontsize = 18)
	plt.ylabel('normalized traffic migration', fontsize = 18)
	plt.annotate('', xy=(1.00033, 0.163429), xytext=(1.04, 0.17), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.00033, 0.175875), xytext=(1.04, 0.17), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.00033, 0.212964), xytext=(1.04, 0.17), arrowprops=dict(arrowstyle="->"))
	plt.text(1.04214, 0.169, 'default points', fontsize = 18)
	plt.annotate('', xy=(1.201, 0.0677542), xytext=(1.15, 0.119), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.201, 0.075051), xytext=(1.15, 0.119), arrowprops=dict(arrowstyle="->"))
	plt.annotate('', xy=(1.201, 0.0942021), xytext=(1.15, 0.119), arrowprops=dict(arrowstyle="->"))
	plt.text(1.10, 0.1219, 'minimum migration points', fontsize = 18)
	plt.grid(True)
	plt.show()

if __name__ == '__main__':
	#energy()
	#lifetime()
	#migration()
	pareto_lifetime()
	#pareto_migration()