from string import *
from itertools import product
value = ascii_letters + digits + punctuation
value
for i in range (1,4):
 for j in product (value,repeat = i):
    word = "".join(j)
    p = open("password1.txt", "a" )
    p.write (word)
    p.write('\n')
    print(word)