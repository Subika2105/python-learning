username = input("Enter you name: ")
print("Your name is" + username + " this is test")
print(f"Your name is {username} , this is test")

price = 51
txt = f"It is very {'Expensive' if price > 50 else username}"

print(txt)