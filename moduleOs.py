import os

#Define Argument
wd = os.getcwd()
filelist = os.listdir(wd)

#Using
print('Current Directory is : ' + wd)
for i in filelist:
    if os.path.isfile(i) == True:
        print('The file : ' + i + ' has ' + str(os.path.getsize(i)) + ' Bytes ')
    elif os.path.isdir(i) == True:
        print('The directory : ' + i + ' has ' + str(os.path.getsize(i)) + ' Bytes ')
