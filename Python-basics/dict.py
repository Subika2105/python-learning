#simple dictionary(mutable)
my_dict={"name:subi","age:20","city:tirupur"}
print(my_dict)
#accessing dictionary values
student = {
    "name": "Kavi",
    "age": 21
}
print(student["name"])
#adding new key-value pair
student["city"]="tirupur"
print(student)
#removing key value pair
student={"name":"kavi","age":21,"city":"tirupur"}
student.pop("age")
print(student)
#update values
student = {
    "name": "Abi",
    "age": 20
}
student.update({"age": 21})
print(student)
#looping thrugh dictionary
student = {
    "name": "Abi",
    "age": 20,
    "city": "Chennai"
}
for i in student.keys():
    print(i)
    for j in student.values():
        print(j)
        #check if statement exists 
        if "native"in student:
            print("present")
        else:
            print("absent")
            