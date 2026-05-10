#simple list(mutable)
fruits = ["apple", "banana", "mango"]
print(fruits)

# Access list items (indexing)
a=["pappaya","grapes","orange"]
print(a[1])
#negative indexing
print(a[-2])

#slicing
animals=["cat","dog","tiger","lion"]
print(animals[0:2])
#replace the valu
animals[0]= "goat"
print(animals)
#add item to the list
animals.append("parrot")
print(animals)
#loop thrugh the list
for i in animals:
    print(i)
#check if item exists in the list
if"goat" in animals:
    print("present")
else:
    print("absent")
