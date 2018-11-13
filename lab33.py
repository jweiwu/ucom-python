from datetime import datetime

now = datetime.now()
print "now with repr:", repr(now)
print "now with str:", str(now)
print now
print (now,)
print "remember the comma", (now)
print [now, ]
print [str(now), ]
print {now, }
print {'key': now}
