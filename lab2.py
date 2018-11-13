def getDigit(x):
    returnDigit = 0
    while x > 0:
        x //= 10
        returnDigit += 1
    return returnDigit

print getDigit(12345)
print getDigit(1234567)
print (2**512)
print getDigit((2**512))