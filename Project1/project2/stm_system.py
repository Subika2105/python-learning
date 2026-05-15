student = []

def add_student():
    name = input("enter your name:")
    age = input("enter your age:")
    student_record = {"name": name,
                      "age": age}
    student.append(student_record)
    print(student_record)

def view_student():
    for record in student:
        print(record)

def search_student():
    student_name = input("enter your name:")
    for record in student:
        if record["name"] == student_name:
            print(record)
            return
    print("student not found")

def delete_student():
    student_name = input("enter your name:")
    for record in student:
        if record["name"] == student_name:
            student.remove(record)
            print("deleted")
            return
    print("student not found")

while True:
    print("1.add")
    print("2.view")
    print("3.search")
    print("4.delete")
    print("5.exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
