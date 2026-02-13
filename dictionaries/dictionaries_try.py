student = {
    "name": "Alex",
    "age": 21,
    "grades": [88, 92, 79]
}


print(student["name"])
student["city"] = "Manila"


student["average"] = sum(student["grades"]) / len(student["grades"])

if student["average"] > 75:
    print("Passed")

else:
    print("Failed")

print(student)


