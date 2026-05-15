balance = 1000
def check_balance():
    print("the balance is:",balance)
def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Amount Deposited")
def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if balance<=amount:
        balance = balance-amount
        print("amount sufficient")
    else:
        print("amount insufficient")

while True:
    print("1.check balance")
    print("2.withdraw")
    print("3.deposit")
    print("4.exit")

    choice = input("enter your choice:")
    if choice == "1":
        check_balance()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        deposit()
    elif choice == "4":
        print("thank you")
        break
    else:
        print("invalid")


     