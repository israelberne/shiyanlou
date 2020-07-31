import sys
import os
def search(root, target):
    items = os.listdir(root)
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            print('[-]', path)
            search(path, target)
        elif path.split('/')[-1] == target:
            print('[+]', path)
        else:
            print('[!]', path)

if len(sys.argv) != 3:
    print('[Usage]:python3 RecursiveFile.py root target')
else:
    search(sys.argv[1],sys.argv[2])
