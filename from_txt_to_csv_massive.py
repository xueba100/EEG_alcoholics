#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#This part create a list that holds all txt file names in the diretory of which the path is manually put in.
import time
time_start = time.time()
import os
dirpath=input('Give me a directory path here.\neg.H:/DataSet/EEG/alcoholics/co2a0000364/')
list_name = []
for file in os.listdir(dirpath):
    file_path = os.path.join(dirpath, file)
    if os.path.splitext(file_path)[1]=='.txt':
        list_name.append(file_path)
print('File name list generated. Check list_name for file names.')


import linecache
for path in list_name:
    list_ = []
    if os.path.exists(path) is False:
        print("Error: There is no such file.Quiting...")
        os._exit()
    else:
        print(path, 'processing started.\n\nVacant lines will be dropped in final result')
        for i in range(17000):
            line = linecache.getline(path, i)
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
    print('Now all the data are pushed in a list called list_ as lines of strings.')


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



    csvpath = path[:-3] + 'csv'
    import csv
    with open(csvpath,'w',newline = '') as csvfile:#没有newline=''，每两行之间会多一个空行
        writer = csv.writer(csvfile)
        writer.writerow(["Trial","Electrode","Channel","Voltage"])
        for i in range(len(datalist)):
            writer.writerow(datalist[i])
        csvfile.close()
        print("csv file generation finished.")
        print(path, 'processing finished.')
print('All finished.')
time_end = time.time()
time = time_end - time_start
print('Excution time:',time,'s')
