list1 = []
list2 = []
distance = 0
totalDistance = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        list1.append(int(line[0:5]))
        list2.append(int(line[8:13]))

#print(list1)
#print(list2)
list1.sort()
list2.sort()
#print(list1)
#print(list2)

for number in range(len(list1):
    distance = abs(list1[number] - list2[number])
    totalDistance += distance
    
print(totalDistance)
