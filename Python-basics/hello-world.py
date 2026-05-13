# Function with parameters and return value
def add(a, b):
    return a + b # returning the sum of a and b
result = add(10, 20) # calling the function and storing the result in a variable

#print("The sum is:", result) # printing the result

#function  parameters and without return value
# def display(a, b):
#     print("The value of a is:", a)
#     print("The value of b is:", b)
# display(result, 20)

def checkStringLength(text):
  count = 0
  for i in text:
      count = count + 1
  return count

text = "Hello"

result = checkStringLength(text)

print(result)
print(len(text))
