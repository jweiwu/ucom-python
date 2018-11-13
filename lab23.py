dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
lengths = []
for day in dayOfWeek:
    lengths.append(len(day))
print lengths

print [len(day) for day in dayOfWeek]
print [day for day in dayOfWeek if len(day) > 7]
sun, mon, tue, wed, thr, fri, sat = dayOfWeek
print sun, tue, fri
print mon, wed, sat
