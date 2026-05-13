a=2
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
#number variable
a=10
b=10
print(a)
print(b)
#string variable
a="gm"
print(a)
#string concatenation
x="subi"
y="subramani"
print(x+y)
#string with space
x="subi"
y="subramani"
print(x+" "+y)
#this is my first program(list)
fruits =["apple","banana","cherry"]
for x in fruits:
    print(x)
    
    #tuple
    fruits =("apple","banana","cherry")
    print(fruits)

    #set
    a={"mouse","key","monitor"}
    print(a)
    if "mouse" in a:
        print("mouse is print")
    else:
        print("mouse is absent")

        #integer to float
        a=19
        print(float(a))
        int=int(input("enter the number: "))
        print(int)
        #dictionary
        a={"name":"subiii","age":20,"city":"chennai"}
        print(a["name"])
        print(a["age"])
        print(a["city"])

    #basic syntax
    a=20
    print(a)
    #single line
    print('hello world')
    print('good morning')
    #mutline line
    a='''python is the high level programming language
        easy to learn and understand for the users'''
    print(a)

    #string concatenation
    a="python"
    b="programming"
    print(a+" "+b)

    #string indexing
    a="hello"
    print(a[1])
    print(a[2])

    #length of the string
    a="welcome to python"
    print(len(a))

    #string slicing
    a="good morning"
    print(a[0:1])

    #string methods
    a="virat kohli"
    print(a.upper())
    print(a.lower())
    print(a.capitalize())
    print(a.replace("v","s"))
    print(a.split(" "))
    print(a.startswith("v"))
    print(a.endswith("i"))

    #set
    a={"apple","banana","cherry"}
    print(a)
    #if condition
    if "apple" in a:
        print("present")
    else:
        print("absent")

    #add item
    a={"apple","orange"}
    a.add("banana")
    print(a)
    #remove item
    a={"apple","orange","banana"}
    a.remove("orange")
    print(a)
    #union of sets
    set1={"apple","orange"}
    set2={"banana","apple"}
    print(set1|set2)
    #intersection of sets
    print(set1&set2)
    #difference of sets
    print(set1-set2)
    #symmetric difference of sets
    print(set1^set2)
    
    #python casting
    a=20
    print(float(a))
    b=2.3
    print(int(b))
    k=200
    print(str(k))
    d=10
    print(bool(d))

    #tuple
    a=("key","mouse","map")
    print(a)
    #count
    a=("key","mouse","map")
    print(a.count("key"))
    #index
    a=("key","mouse","map")
    print(a.index('mouse'))

    #list
    a=[1,2,3]
    b=[4,5,6]
    print(a+b)
    #append
    a=[1,2,3]
    a.append(4)
    print(a)
    #remove
    a=[1,2,3,4,5]
    a.remove(3)
    print(a)
    #insert
    a=[1,2,3]
    a.insert(7,2)
    print(a)

    #for loop
    a=("p","a","s")
    for i in a:
        print(i)
    
    #break statement
    a=(1,2,3,4)
    for i in a:
        if i==1:
            break
        print(i)
    
    #dictionary
    my_set={"name: subi","age:19","city: tirupur"}
    print(my_set)
    #add
    my_set.update({"age: 20"})
print(my_set)

#for loop(repeated code for each item)
word = "python"
for i in word:
    print(i)
#sum of numbers
total = 0
for i in range(1,6):
    total = total + i
print(total)

#while loop(while loop used to:repeat code while condition is TRUE)
i = 5
while i >= 1:
    print (i)

#another example
i=1
while i <=2:
    print(i)
    i=i+1
#another example
password = ""
while password != "python":
    password = input("Enter password: ")
print("Correct Password")

#new practice from starting(comments)
# My details
name = "Subika"
age = 21
print(name)
print(age)
#variable
a="python"
s="21"
print(a)
print(s)

name = input("Enter your name: ")
print(name)




 
     


    






    
        
    
