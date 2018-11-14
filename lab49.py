import csv

sampleFile = open('.\\data\\csv1.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
sampleFile.close()

print len(sampleData), type(sampleData)
for item in sampleData:
    print type(item), item
