import math
import random

# random.seed(2019)
print math.pi, math.log(2), math.sqrt(5)
for i in range(0, 1000):
    print random.randint(1, 500),
print ""
l1 = ['Macdonald', "KFC", "Burger King", "Pizza Hut"]
print random.choice(l1)
l2 = [2, 3, 4, 5, 6, 7, 8, 9, 'j', 'q', 'k', 'a']
random.shuffle(l2)
print l2
