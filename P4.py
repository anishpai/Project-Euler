#Project Euler
#P4: Find the largest palindrome made from the product of two 3-digit numbers

def palin_number():
    rnge = range(100,1000)
    palin = 0
    for i in rnge:
        for j in rnge:
            prod = i*j
            if str(prod) == str(prod)[::-1]:
                if prod > palin:
                    palin=prod
    return palin

print(palin_number())


