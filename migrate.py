#!usr/bin/env python
#-*- coding:utf-8 -*-

# this model is for calculating data migration
# JialongLi 2016/11/14

import random
import copy 
from GA_2 import first_fit
from GA_2 import eval_func
from test_2 import first_fit_init

CASE = 100
DAY = 30
ONU_NUM = 64 * 4
WAVE_NUM = 32
CAPACITY = 3.0 * 4
EVENT = 24 * CASE * DAY

# calculating total traffic
def cal_total_traffic(file_traffic):
	traffic = []
	total_traffic = 0;
	for i in range(EVENT):
		traffic_line = file_traffic.readline().decode('utf-8')
		current_traffic = [float(traffic_line.split()[j]) for j in range(ONU_NUM)]
		traffic.append(current_traffic)
		for value in current_traffic:
			total_traffic += value
	return total_traffic, traffic

def random_fit_traffic(file_traffic, file_list_binpack):
	random_total_traffic = 0
	list_00 = []
	result_random = []

	for i in range(EVENT):
		line_00 = file_list_binpack.readline().decode('utf-8')
		list_00.append(int(line_00.split()[0]))

	for i in range(EVENT):
		traffic_line = file_traffic.readline().decode('utf-8')
		current_traffic = [float(traffic_line.split()[j]) for j in range(ONU_NUM)]
		virtual_numof_bins = list_00[i]
		numof_bins = list_00[i]

		if i == 0:
			old_chromosome = first_fit_init(virtual_numof_bins, current_traffic)
			result_random.append(0)
			continue
		new_chromosome = first_fit(old_chromosome, current_traffic, virtual_numof_bins, numof_bins)
		score = eval_func(new_chromosome, old_chromosome, current_traffic)
		old_chromosome = new_chromosome
		result_random.append(score)
	for value in result_random:
		random_total_traffic += value
	return random_total_traffic

# naive approach: only calculates the traffic out of bound or traffic in shutting down bins
# return a new_chromosome
def migrate_outof_bound(old_chromosome, current_traffic, virtual_numof_bins, numof_bins):
	new_chromosome = copy.deepcopy(old_chromosome)
	pre_pack_onu = set()
	old_numof_bins = len(old_chromosome)
	is_pack = True
	burden_wave = {}

	for key, value in old_chromosome.items():  # adding the current onu in the same bin by decreasing
		burden_wave[key] = 0.0
		is_beyond = False
		temp_wave = {}
		#temp_wave = []
		for onu in value:
			temp_wave[onu] = current_traffic[onu]
			#temp_wave.append(onu)
		temp_wave = sorted(temp_wave.items(), key = lambda e:e[1], reverse = True)

		for item in temp_wave:
			if not is_beyond:
				if burden_wave[key] + current_traffic[item[0]] <= CAPACITY:
					burden_wave[key] += current_traffic[item[0]]
				else:
					is_beyond = True
			else:
				pre_pack_onu.add(item[0])
				new_chromosome[key].remove(item[0])

	if old_numof_bins > numof_bins:    # use less bins
		shutdown_bins = old_numof_bins - numof_bins
		burden_wave_temp = copy.deepcopy(burden_wave)
		burden_wave_temp = sorted(burden_wave_temp.items(), key = lambda e:e[1])
		for i in range(shutdown_bins):
			delete_key = burden_wave_temp[i][0]
			burden_wave.pop(delete_key)
			for item in new_chromosome[delete_key]:
				pre_pack_onu.add(item)
			new_chromosome.pop(delete_key)
	else:							   # use the same or more bins
		extra_bins = numof_bins - old_numof_bins
		for i in range(extra_bins):
			for i in range(WAVE_NUM):
				if i not in new_chromosome.keys():
					burden_wave[i] = 0
					new_chromosome[i] = []
					break
	
	'''
	if len(pre_pack_onu) != 0:		# using best fit algorithm to pack pre_pack_onu
		pre_pack_onu_list = {}
		for item in pre_pack_onu:
			pre_pack_onu_list[item] = current_traffic[item]
		pre_pack_onu_list = sorted(pre_pack_onu_list.items(), key = lambda e:e[1], reverse = True)
		for i in range(len(pre_pack_onu)):
			onu_key = pre_pack_onu_list[i][0]
			is_found = False
			wave_max_burden = 0
			pack_wave = 0
			for key, value in burden_wave.items():
				if value + current_traffic[onu_key] <= CAPACITY and value > wave_max_burden:
					wave_max_burden = value
					pack_wave = key
					is_found = True
			if is_found:
				new_chromosome[pack_wave].append(onu_key)
				burden_wave[pack_wave] += current_traffic[onu_key]
				is_pack = True
			else:
				is_pack = False
				break
	'''
	
	if len(pre_pack_onu) != 0:		# using first fit algorithm to pack pre_pack_onu
		for i in pre_pack_onu:
			onu_key = i
			is_found = False
			pack_wave = 0
			for key, value in burden_wave.items():
				if value + current_traffic[onu_key] <= CAPACITY:
					pack_wave = key
					new_chromosome[pack_wave].append(onu_key)
					burden_wave[pack_wave] += current_traffic[onu_key]
					is_found = True
					break
			if is_found:
				is_pack = True
			else:
				is_pack = False
				break
	
	
	'''
	if numof_bins > virtual_numof_bins:
		if len(pre_pack_onu) != 0:		# using first fit algorithm to pack pre_pack_onu
			pre_pack_onu_list = {}
			for item in pre_pack_onu:
				pre_pack_onu_list[item] = current_traffic[item]
			pre_pack_onu_list = sorted(pre_pack_onu_list.items(), key = lambda e:e[1], reverse = True)
			for i in range(len(pre_pack_onu)):
				onu_key = pre_pack_onu_list[i][0]
				is_found = False
				pack_wave = 0
				for key, value in burden_wave.items():
					if value + current_traffic[onu_key] <= CAPACITY:
						pack_wave = key
						new_chromosome[pack_wave].append(onu_key)
						burden_wave[pack_wave] += current_traffic[onu_key]
						is_found = True
						break
				if is_found:
					is_pack = True
				else:
					is_pack = False
					break
	else:
		if len(pre_pack_onu) != 0:		# using first fit algorithm to pack pre_pack_onu
			pre_pack_onu_list = {}
			for item in pre_pack_onu:
				pre_pack_onu_list[item] = current_traffic[item]
			pre_pack_onu_list = sorted(pre_pack_onu_list.items(), key = lambda e:e[1], reverse = False)
			for i in range(len(pre_pack_onu)):
				onu_key = pre_pack_onu_list[i][0]
				is_found = False
				pack_wave = 0
				for key, value in burden_wave.items():
					if value + current_traffic[onu_key] <= CAPACITY:
						pack_wave = key
						new_chromosome[pack_wave].append(onu_key)
						burden_wave[pack_wave] += current_traffic[onu_key]
						is_found = True
						break
				if is_found:
					is_pack = True
				else:
					is_pack = False
					break
	'''
	'''
	if numof_bins == virtual_numof_bins:
		if random.random() < 0.0:
			is_pack = False
	'''
	if not is_pack:
		new_chromosome = first_fit(old_chromosome, current_traffic, virtual_numof_bins, numof_bins)

	return new_chromosome


# calculating the migration
def cal_migrate_outof_bound(traffic, list_binpack, list_real):
	migrate_traffic_real = 0
	result = []

	for i in range(EVENT):
		current_traffic = traffic[i]
		virtual_numof_bins = list_binpack[i]
		numof_bins = list_real[i]
		if i == 0:
			old_chromosome = first_fit_init(virtual_numof_bins, current_traffic)
			result.append(0)
			continue
		new_chromosome = migrate_outof_bound(old_chromosome, current_traffic, virtual_numof_bins, numof_bins)
		score = eval_func(new_chromosome, old_chromosome, current_traffic)
		old_chromosome = new_chromosome
		result.append(score)
		'''
		onu_length = 0
		for key, value in new_chromosome.items():
			onu_length += len(value)
		print onu_length
		'''
		#print len(new_chromosome)
	for value in result:
		migrate_traffic_real += value

	return migrate_traffic_real

if __name__ == '__main__':
	MAX_PERIOD = 7
	MAX_RESERVATION = 5
	sigma_num = 1
	repeat_time = 3

	for m in range(1, sigma_num + 1):
		for n in range(1, repeat_time + 1):
			print 'm = ' + str(m) + '\t' + 'n = ' + str(n)
			file_traffic_path = './data/traffic_data_' + str(m) + str(n) + '.txt'
			file_migrate_path = './data/migrate_' + str(m) + str(n) + '.txt'
			file_list_real_path = './data/reserve_' + str(m) + str(n) + '.txt'
			file_list_binpack_path = './data/binpack_' + str(m) + str(n) + '.txt'

			file_traffic = open(file_traffic_path, 'r')
			file_migrate = open(file_migrate_path, 'w')
			file_list_real = open(file_list_real_path, 'r')
			file_list_binpack = open(file_list_binpack_path, 'r')	

			# calculating total traffic
			total_traffic, traffic = cal_total_traffic(file_traffic)
			print "total_traffic" + '\t' + str(total_traffic)
			file_traffic.close()
			file_migrate.write("total_traffic" + '\t' + str(total_traffic) + '\n')

			# calculating migrated traffic   # binpack
			list_binpack = [0 for i in range(EVENT)]
			list_real = [0 for i in range(EVENT)]
			for i in range(EVENT):
				line = file_list_binpack.readline().decode('utf-8')
				list_binpack[i] = int(line.split()[0])

			list_real = copy.deepcopy(list_binpack)
			migrate_traffic_00 = cal_migrate_outof_bound(traffic, list_binpack, list_real)
			print "migrate_traffic_00" + '\t' + str(migrate_traffic_00)+ '\t' + str(migrate_traffic_00 / total_traffic)

			file_list_binpack.close()
			file_migrate.write("migrate_traffic_00" + '\t' + str(migrate_traffic_00) + '\t' + str(migrate_traffic_00 / total_traffic) + '\n')
			
			# calculating migrated traffic   # reserve
			for wave in range(1, MAX_RESERVATION + 1):
				for period in range(1, MAX_PERIOD + 1):
					for i in range(EVENT):
						line = file_list_real.readline().decode('utf-8')
						list_real[i] = int(line.split()[0])

					migrate_traffic = cal_migrate_outof_bound(traffic, list_binpack, list_real)
					print "migrate_traffic_" + str(wave) + str(period) + '\t' + str(migrate_traffic)+ '\t' + str(migrate_traffic / total_traffic)
					file_migrate.write("migrate_traffic_" + str(wave) + str(period) + '\t' + str(migrate_traffic) + '\t' + str(migrate_traffic / total_traffic) + '\n')
			
			file_list_real.close()
			file_migrate.close()
	
	

	