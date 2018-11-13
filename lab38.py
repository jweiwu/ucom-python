# pip install requests
# pip install bs4
# https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?utm_source=chrome-ntp-icon
import requests

url1 = "https://bugzilla.mozilla.org/rest/bug/35"
result1 = requests.get(url1)
print result1.status_code, result1.content
print type(result1.content), result1.content[:50]
print type(result1.json())
bugs = result1.json()["bugs"]
for bug in bugs:
    print type(bug), bug
    assign_to = bug["assigned_to"]
    print "assign to==>", assign_to
