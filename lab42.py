import requests
import urllib2
from bs4 import BeautifulSoup

url1 = "https://www.mobile01.com/"
# id==4,2,5
ids = [2, 4, 5]
for id in ids:
    print '[ Category ID = %s ]' % id
    url2 = "https://www.mobile01.com/category.php?id=%d" % (id)
    USERAGENT = 'Mozilla/5.0'
    req = urllib2.Request(url2)
    req.add_header("User-agent", USERAGENT)
    soup1 = BeautifulSoup(urllib2.urlopen(req), "html.parser")
    print type(soup1)
    # print soup1
    hot = soup1.find('div', {'id': 'hot-posts'})
    # print hot
    items = hot.find_all('a')
    for item in items:
        print item.text
    print '\n'
