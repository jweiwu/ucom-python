# encoding=UTF-8
import shutil
import json

# shutil.copytree('data', 'clone')
# shutil.rmtree('clone')

data1 = ['hello', 'world', 100, 50, 3.14, 'hihi', 'いゅ']
string1 = json.dumps(data1)
print string1
data2 = {"course": 'BDPY', 'duration': 35, 'location': 'TPE'}
string2 = json.dumps(data2)
print string2
return1 = json.loads(string1)
print type(return1), return1[6]
return2 = json.loads(string2)
print type(return2), return2['duration']
