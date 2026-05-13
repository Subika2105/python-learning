#simple set operations
my_set={1,2,3,4,5,6}
print(my_set)
#add element to set
my_set.add(7)
print(my_set)
#remove element from set
my_set.remove(3)
print(my_set)
#union of sets
set1={1,2,3}
set2={3,4,5}
print(set1|set2)
#intersection of sets
print(set1&set2)
#difference of sets
print(set1-set2)
#symmetric difference of sets
print(set1^set2)
#if condition
if 9 in my_set:
    print("present")
else:
    print("absent")
#loop through the set
my_set={1,2,3,4,5}
for i in my_set:
    print(i)
#length of the set
my_set={"hello"}
print(len(my_set))



