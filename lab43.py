import requests

url = 'https://pythonucom.firebaseio.com/%s.json'
url7 = url % 'orders'
for i in range(0, 20):
    bid = {'name': 'Mark', "price": 700 + 50 * i}
    result7 = requests.post(url7, json=bid)
    print result7.status_code, result7.json()
