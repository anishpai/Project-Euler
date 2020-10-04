#Project Euler
#P22: Name Scores



f = open('p22_names.txt')
words = f.read().replace('"', '').split(',')
words = sorted(words)

#print(words)
index = 1
sums = 0
for w in words:

    word_score = 0
    for char in w:
        word_score += (ord(char)-64)

    sums += index*word_score
    
    index += 1

print(sums)
    

