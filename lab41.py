# encoding=UTF-8
# https://firebase.google.com
import requests

url = 'https://pythonucom.firebaseio.com/%s.json'
url1 = url % ('string1')
string1 = "[11-13]hello world"
result1 = requests.put(url1, json=string1)
print result1.status_code, result1.json()
url2 = url % ('chinese1')
string2 = '試試中文'
result2 = requests.put(url2, json=string2)
print result2.status_code, result2.json()
url3 = url % ('utf1')
string3 = u'試試中文'
result3 = requests.put(url3, json=string3)
print result3.status_code, result3.json()
url4 = url % ('list1')
list4 = ['A', 'B', '中文', None, "Hello World", 3.14]
result4 = requests.put(url4, json=list4)
print result4.status_code, result4.json()
url5 = url % ('dict1')
dict5 = {'course': 'python實務', 'duration': 35, 'location': '台北'}
result5 = requests.put(url5, json=dict5)
print result5.status_code, result5.json()
item6 = {'part': 'm3 nut', 'quantity': 500}
url6 = url % ('spare/notebook/13u/parts/nut')
result6 = requests.put(url6, json=item6)
print result6.status_code, result6.json()
