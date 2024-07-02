numbers = [1,1,2,3,4]
#convert a list to a set
uniques = set(numbers)
print(uniques)

#create a set
second = {1, 4}
#add items
second.add(5)
print(second)
#length of a set
print(len(second))

#mathematical operations on set
set1 = {1, 2, 3, 5}
set2 = {6, 2, 4, 7}
#union of two sets
print(set1 | set2)
#intersection of two sets
print(set1 & set2)
#difference between two sets
print(set1 - set2)
#symetric difference
print(set1 ^ set2)

#membership
if 1 in set1:
    print("1 is here!")