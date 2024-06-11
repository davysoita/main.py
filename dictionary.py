# python programm to create dictionary
student={
    "name":"david",
    "reg_no":13910,
    "age":34,
    "email":"davysoita@gmail.com",
    "course":"BSCIT",
    "country":"kenya",
    "county":"trans nzoia",
    "school":"kitale national polytechnic",
    "school_level":"technical and vocational training",
    "level":"Diploma"
}
student["name"]="soita"
print(student)
print(student["name"])
print(student.values())
print(student.keys())
print(student.items())
for i in student.keys():
    print(i)
for values in student.values():
    print(values)
for key, values in student.items():
    print(key, values)
print(student)