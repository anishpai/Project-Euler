#Project Euler
#P3: What is the largest prime factor of the number 600851475143?

number = int(input("Number: "))
n= number
factors =[]

while number%2 == 0:
    factors.append(2)
    number //=2

divisor = 3
while number !=1 and divisor <=number:
    if number % divisor ==0:
        factors.append(divisor)
        number //=divisor
    else:
        divisor +=2

for i in range(len(factors)):
    print(factors[i])
    
print("The largest prime factor of a the number: " +str(n) + " is " + str(max(factors)))
