#coding:utf-8
#这是批量修改文件名的程序
import os

pathway = input('Give me a directory path here.Files in this folder will be walked through.\neg.H:/DataSet/EEG/alcoholics/co2c0000363/')
path = pathway[:-2]
file_name = os.listdir(pathway)#需要修改的文件在哪个文件夹里，绿色部分就写哪里
L = []

for temp in file_name: #对于文件夹里的文件
    L = os.path.splitext(temp) #分离扩展名：os.path.splitext(r"c:\python\hello.py") --> ("c:\\python\\hello", ".py")
    if L[-1]=='.txt' or 'csv':#对于txt和csv格式的文件
        new_name = temp
        if L[0][0]=='#':#如果名字第一个字是’#‘
            new_name = temp[2:]#去掉前两个字符
        #去掉文件名中的.rd
        for i in range(len(new_name)):
            if (new_name[i] == '.')and(new_name[i+1]=='r')and(new_name[i+2]=='d') :
                new_name = new_name[:i] + new_name[i+3:]
                break#这里是跳出了if结构
        if os.path.exists(pathway+new_name) is False:
            os.rename(pathway +temp, pathway + new_name)#重命名：os.rename(old name, new name)
 
