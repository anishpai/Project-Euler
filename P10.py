#PROJECT EULER
#P10: Sum of prime below two million


#from math import sqrt
#def isPrime(n):
#
#    if n<=1:
#        return False
#
#    for i in range(2,int(sqrt(n))):
#        if n %i ==0:
#            return False
#
#    return True
#
#def nPrime(n):
#    sums = 0
#    for i in range(2,n+1):
#        if isPrime(i):
#            print(i,end = " ")
#            sums = sums + i
#    print(sums)
#
#if __name__ == "__main__":
#    n = 2000000
#    nPrime(n)

# Using Sieve of Eratosthenes the program runs faster

def eras(n):
    multiples = set()

    for i in range(2,n+1):

        if i not in multiples:

            yield i

            multiples.update(range(i*i, n+1, i))

sums = 0
ml = list(eras(2000000))
for x in ml:
    sums = sums + int(x)
print(sums)
