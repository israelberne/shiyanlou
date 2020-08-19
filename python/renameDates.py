import shutil, os, re

datePattern = re.compile(r'''
        (^.*?)
        ([0-1]?\d)-
        ([0-3]?\d)-
        ((19|20)\d\d)
        (.*$)
        ''',re.VERBOSE)

for usFilename in os.listdir('.'):
    mo = datePattern.search(usFilename)

    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    euFilename = (beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart)
    absWorkingDir = os.path.abspath('.')
    usFilename = os.path.join(absWorkingDir,usFilename)
    euFilename = os.path.join(absWorkingDir,euFilename)

    print('Renaming {} to {}'.format(usFilename,euFilename))
    shutil.move(usFilename,euFilename)
