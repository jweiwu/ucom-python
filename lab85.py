import sqlite3
import time

connection1 = sqlite3.connect('.\\data\\lab90.sqlite')

emp1 = {'NAME': "Mark", 'AGE': 43, 'DEPT': 1, 'ADDR': 'Taipei'}
emp2 = {'NAME': "John", 'AGE': 46, 'DEPT': 2, 'ADDR': 'Hsinchu'}
emp3 = {'NAME': "Ken", 'AGE': 39, 'DEPT': 1, 'ADDR': 'Taichung'}
emp4 = {'NAME': "Tim", 'AGE': 47, 'DEPT': 2, 'ADDR': 'Kaohsiung'}

employees = [emp1, emp2, emp3, emp4]

sql_dml = "INSERT INTO EMPLOYEE (NAME, AGE, DEPT, ADDRESS) values (?,?,?,?)"
start_time = time.time()
for i in range(1000):
    for e in employees:
        # print 'e=', e
        connection1.execute(sql_dml, (e['NAME'], e['AGE'], e['DEPT'], e['ADDR']))
        connection1.commit()
# connection1.commit()
print "---%s seconds---" % (time.time() - start_time)
connection1.close()
