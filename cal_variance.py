#!usr/bin/env python
#-*- coding:utf-8 -*-

# this model is for calculating variance
# JialongLi 2016/12/08
import math

def calculate_variance(file_traffic):
	ONU_NUM = 64
	TEST_NUM = 1
	HOUR_NUM = 24
	variance = []
	total_traffic = []
	for i in range(TEST_NUM):
		traffic_hour = []
		for j in range(HOUR_NUM):
			traffic_onu = 0
			line = file_traffic.readline().decode('utf-8')
			for k in range(ONU_NUM):
				traffic_onu += float(line.split()[k])
			traffic_hour.append(traffic_onu)
		
		total = 0
		for j in range(HOUR_NUM):
			total += traffic_hour[j]
		total_traffic.append(total)
		average = total / HOUR_NUM
		total_squre = 0
		for value in traffic_hour:
			total_squre += (value - average) * (value - average)
		variance.append(total_squre / HOUR_NUM)
	for i in range(HOUR_NUM):
		traffic_hour[i] = float('%.2f' % traffic_hour[i])
	return traffic_hour, variance

def cal_basic_variance():
	HOUR_NUM = 24
	ONU_NUM = 64
	basic_traffic = [0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.40, 0.60, 1.00, 1.00, 1.00, 1.00, 1.00, \
	1.00, 1.00, 1.00, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40]
	
	total = 0
	for value in basic_traffic:
		total += value * ONU_NUM
	average = total / HOUR_NUM
	total_squre = 0
	for value in basic_traffic:
		total_squre += (value * ONU_NUM - average) * (value * ONU_NUM - average)
	variance = total_squre / HOUR_NUM
	return total, variance
		


if __name__ == '__main__':
	file_traffic = open('traffic_data_sigma1.txt', 'r')
	total_1, variance_1 = calculate_variance(file_traffic)
	print variance_1, total_1
	file_traffic = open('traffic_data_sigma2.txt', 'r')
	total_2, variance_2 = calculate_variance(file_traffic)
	print variance_2, total_2
	file_traffic = open('traffic_data_sigma3.txt', 'r')
	total_3,variance_3 = calculate_variance(file_traffic)
	print variance_3, total_3

	total, variance = cal_basic_variance()
	print "basic variance: " + str(variance)
	print "basic traffic " + str(total)