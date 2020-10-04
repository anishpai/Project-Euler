#PROJECT EULER
#P20: Factorial Digit Sum





fact = 1

for i in range(1,100+1):
    fact = fact*(i)
print(fact)

sum_of_digits = 0

for digit in str(fact):


  sum_of_digits += int(digit)
print("-------------------")
print(sum_of_digits)






#print(digit_sum)

