import requests

url = 'https://pythonucom.firebaseio.com/%s.json'
url1 = url % 'string1'
result1 = requests.get(url1)
print result1.json()
url2 = url % 'chinese1'
result2 = requests.get(url2)
print result2.json()
url4 = url % 'list1'
result4 = requests.get(url4)
print result4.json()[2]
url5 = url % 'dict1'
result5 = requests.get(url5)
print result5.json()["location"]
url7 = url % 'orders'
result7 = requests.get(url7)
print type(result7.json())
records = result7.json()
for v in records.values():
    print "owner=%s, price=%s" % (v["name"], v["price"])
    # for k1, v1 in v.items():
    #     print "[%s]%s"%(str(k1), v1)
