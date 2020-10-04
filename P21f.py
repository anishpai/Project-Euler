
import time, math
'''
start = time.time()

amicable_nums = set()

def sum_div(n):
    divisors = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            divisors.append(x)

            if x * x != n and x != 1:
                divisors.append(int(n / x))
    return sum(divisors)

for i in range(1, 10000):
    for j in range(1, 10000):
        if sum_div(i) == j and sum_div(j) == i and i != j:
            amicable_nums.update([i, j])

print(sum(amicable_nums))
print("It took " + str(time.time() - start) + " seconds")
'''

def sum_div(n):
    total = 1
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            total += x
            y = n // x
            if y > x:
                total += y
    return total

def amicable_numbers(limit):
    for a in range(limit):
        b = sum_div(a)
        if a != b and sum_div(b) == a:
            yield a

print(sum(amicable_numbers(10000)))

