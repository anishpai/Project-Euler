#PROJECT EULER
#P16: What is the sum of the digits of the number 21000?

import math

a = [int(i) for i in str(2**1000)]
print(a)

count = 0
for i in a:
    count = count+i

print(count)


