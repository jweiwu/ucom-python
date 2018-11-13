import requests

url = 'https://pythonucom.firebaseio.com/%s.json'
url7 = url % 'orders'
result7 = requests.delete(url7)
print result7.status_code
url6 = url % 'spare'
result6 = requests.delete(url6)
print result6.status_code
