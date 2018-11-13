import requests
from bs4 import BeautifulSoup

url1 = "https://www.uuu.com.tw"
result1 = requests.get(url1)
soup1 = BeautifulSoup(result1.content, "html.parser")
print type(soup1)
hot = soup1.find('div', {'id': 'course_list'})
# print hot
items = hot.find_all('div', {'class': 'NormalBOX'})
for item in items:
    print item.find('h3').string
