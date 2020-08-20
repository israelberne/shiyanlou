#Import module
import shutil, os, re

#Create a regex's match object
datePattern = re.compile(r'''
        (^.*?)
        ([0-1]?\d)-
        ([0-3]?\d)-
        ((19|20)\d\d)
        (.*$)
        ''',re.VERBOSE)

#Loop over the files in the working directory.
for usFilename in os.listdir('.'):
    mo = datePattern.search(usFilename)

    #Skip files don't match the pattern.
    if mo == None:
        continue

    #Get different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(6)

    #Form the European-style filename.
    euFilename = (beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart)
    absWorkingDir = os.path.abspath('.')
    usFilename = os.path.join(absWorkingDir,usFilename)
    euFilename = os.path.join(absWorkingDir,euFilename)

    #Rename the files.
    print('Renaming {} to {}'.format(usFilename,euFilename))
    shutil.move(usFilename,euFilename)
