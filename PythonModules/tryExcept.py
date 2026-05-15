#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#another example
try:
    x = int(input("Enter number: "))
    print(x)
except:
    print("Wrong input")
finally:
    print("Done")

#another example
try:
    print(12/2)
except:
   print("not divisible by 2")
finally:
   print("divisible by 2")
   
   
