import cchardet
import sys
import codecs
import os





#Get encoding format of a file.
def findEncoding(s):
    file = open(s, mode='rb')
    buf = file.read()
    result = cchardet.detect(buf)
    file.close()
    return result['encoding']


def convert_Encoding(s):
    encoding = findEncoding(s)
    if encoding != 'utf-8':
        print("convert %s%s to utf-8-sig" % (s, encoding))
        contents = ''
        with codecs.open(s, "r", encoding) as sourceFile:
            contents = sourceFile.read()

        with codecs.open(s, "w", "utf-8-sig") as targetFile:
            targetFile.write(contents)

    else:
        print("%s encoding is %s ,there is no need to convert" % (s, encoding))




#Load txt file names in a list.
dirpath=input('Give me a directory path here.\neg.H:/DataSet/EEG/alcoholics/co2a0000364/')
list_name = []
for file in os.listdir(dirpath):
    file_path = os.path.join(dirpath, file)
    if os.path.splitext(file_path)[1]=='.txt'or '.csv':
        list_name.append(file_path)
print('txt & csv file name list generated. Check list_name for file names.')


#Get file format.
for s in list_name:
    print(s,'\n')
    findEncoding(s)
    convert_Encoding(s)
print(dirpath,'Converted.\n\n\n')
