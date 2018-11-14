# encoding=UTF-8
p = u'中文編碼'
print p.encode('utf8')
print repr(p.encode('utf8'))
print repr(p.encode('big5'))
print repr(p.encode('ms950'))
new_string = '\xe5\xad\x97'
print new_string
new_latin = new_string.decode('latin-1')
print new_latin
new_utf8 = new_string.decode('utf8')
print new_utf8
