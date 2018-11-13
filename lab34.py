# encoding=UTF-8
import os, sys

print os.getcwd()
print os.mkdir("data")
os.chdir('data')
print os.getcwd()
print os.mkdir(u"資料")
os.chdir(u'資料')
print os.getcwd().decode('ms950')
for item in sys.argv:
    print item
