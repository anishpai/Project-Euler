#PROJECT EULER
#P48: Sum of exponential series


import time
start = time.time()


sums =0
for i in range(1,10001):
    a = i**i
    sums = sums + a
    
print(sums)

b = str(sums)
sample = b[-10:]

print(sample)


end= time.time()


print(end - start)
