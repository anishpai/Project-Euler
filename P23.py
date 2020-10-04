#PROJECT EULER
#P23: Non-abundant sums

from math import sqrt

def divisors(n):
    divs=[1]
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    return list(set(divs))

#print(divisors(10))

abundunt_num = []

for i in range(12,28123):
    if sum(divisors(i)) > i:
        abundunt_num.append(i)


non_ab = [x for x in range(28123)]

#print(abundunt_num)

for i in range(len(abundunt_num)):
	for j in range(i,28123):
		if abundunt_num[i]+abundunt_num[j] < 28123:
			#negating the value of the abundant sum
			non_ab[abundunt_num[i]+abundunt_num[j]] = 0
		else:
			break

print(sum(non_ab))
