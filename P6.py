#PROJECT EULER
#P6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

#sum of squares
sm=0
for i in range(1,101):
    sm=sm +(i*i)

print(sm)


#square of sum
n=100
sums=n*(n+1)/2

sums=sums*sums
print(sums)

sqsd = sm- sums
print(sqsd)
