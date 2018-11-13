dayOfWeek = ('sunday', 'monday', 'tuesday')
print hex(id(dayOfWeek))
dayOfWeek += ('wednesday',)
print type(dayOfWeek), hex(id(dayOfWeek)), dayOfWeek
# dayOfWeek += ('thursday',)
print [i for i in dayOfWeek]
print ('Thursday') * 5
print ('Thursday',) * 5
print 'day' in dayOfWeek, 'sunday' in dayOfWeek


def splitHead(seq):
    return seq[0], seq[1:]


dayOfWeekList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

head, remaining = splitHead(dayOfWeekList)
print type(head), head
print type(remaining), remaining
