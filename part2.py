list1 = []
list2 = []
similarity = 0
totalSimilarity = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        list1.append(int(line[0:5]))
        list2.append(int(line[8:13]))

for number1 in list1:
    similarity = 0
    for number2 in list2:
        if number1 == number2:
            similarity += number1
    
    totalSimilarity += similarity
    
print(totalSimilarity)
