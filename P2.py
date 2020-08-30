#Project Euler
#P2:By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Computationally intensive code
##def fib(n):
##    if n<0:
##        print("Enter valid input")
##    elif n==1:
##        return 0
##
##    elif n==2:
##        return 1
##
##    else:
##        return fib(n-1) + fib(n-2)
##    
##n=0
##sum=0
##
##while (fib(n))<4000000:
##    if (((fib(n))%2)==0):
##        sum=sum + fib(n)
##
##print(sum)

#A more efficient implementation

x=1
y=1
z=0
result=0

while z < 4000000:
    z= x+y
    if z%2 ==0:
        result=result + z

    x=y
    y=z

print(result)
print("The sum of the terms in the Fibonacci sequence whose values do not exceed four million,the sum of the even-valued terms is " +str(result))
