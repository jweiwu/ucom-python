# encoding=UTF-8
print '%10s=====' % ('0123456789')
print '%10s=====' % ('PRQST')
print '%-10s=====' % ('PRQST')
print '{:10}====='.format('PQRST')
print '{:>10}====='.format('PQRST')
# take parameter from variable
print '%*s=====' % ((-20), 'PRQST')
