import requests

url = 'https://pythonucom.firebaseio.com/%s.json'
url4 = url % 'list1'
newDict = {'0': 'Apple', '3': 'Donut', '10': 'elephant'}
result4 = requests.patch(url4, json=newDict)
print result4.json()
url5 = url % 'dict1'
newDict2 = {'location': 'TPE ucom', 'instructor': 'MarkHo'}
result5 = requests.patch(url5, json=newDict2)
print result5.json()
