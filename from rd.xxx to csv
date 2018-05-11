#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
time_start = time.time()

import os
dirpath=input('Give me a directory path here.\neg.H:\\DataSets\\Electro\\alcholism\\co2a0000364')
suffix = []
for i in range(120):
    t = str(i)
    if (len(t)== 1):
        suffix.append('.00'+t)
    elif len(t)== 2:
        suffix.append('.0'+t)
    else:
        suffix.append('.'+t)

list_name = []
for file in os.listdir(dirpath):
    file_path = os.path.join(dirpath, file)
    for i in range(0,120):
        if os.path.splitext(file_path)[1]==suffix[i]:
            list_name.append(file_path)

import linecache
import csv

for rd_file in list_name:
    list_ = []
    for i in range(17000):
        line = linecache.getline(rd_file, i)
        if line != '':
            string = ''
            for word in line:
                if word != '':
                    string = string + word
                else:
                    list_.append(string)
                    string = ''
            string = string[:-1]
            list_.append(string)
    print('Now all the data are pushed in a list called list_ with each line as a string.')
    len_list = len(list_)
    datalist = []
    for i in range(5,len_list):#5是数据第一行的行索引值
        list_splited = []
        string = ''
        for word in list_[i]:
            if word != ' ':
                string = string + word
            else:
                list_splited.append(string)
                string = ''
        list_splited.append(string)
        datalist.append(list_splited)
        i = i + 1
    print('Now all the data in this file are stored in a list called "datalist".\n"datalist" is a list composed of lists.')
    print(datalist)
    csvpath = rd_file[:-7] + '-' + rd_file[-3:] + '.csv'
    with open(csvpath, 'w', newline='') as csvfile:  # 没有newline=''，每两行之间会多一个空行
        writer = csv.writer(csvfile)
        writer.writerow(["Trial", "Electrode", "Channel", "Voltage"])
        for i in range(len(datalist)):
            writer.writerow(datalist[i])
        csvfile.close()
        print("csv file generation finished.")
        print(rd_file, 'processing finished.')
print("All finished.")

time_end = time.time()
time = time_end - time_start
print('Excution time:',time,'s')
