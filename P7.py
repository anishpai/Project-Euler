#PROJECT EULER
#P7: What is the 10 001st prime number?

from math import sqrt
def isPrime(x):
    if x < 2:
        return False
    if x==2 or x==3:
        return True
    for i in range(2,int(sqrt(x)) + 1):
        if x % i ==0:
            return False

    return True


def getnPrime(x):
    count=0
    num=2
    while True:
        if isPrime(num):
            count = count +1
            if count == x:
                return num
        num=num+1

print(getnPrime(100))
