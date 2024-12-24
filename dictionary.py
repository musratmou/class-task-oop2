employee = {
    "name": "A",
    "age": 40,
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, True, 7, 1}
}

print(len(employee))
print(type(employee))
print(employee)

# Accessing a nested key
employee["type"] = {"developer": "backend"}
print(employee["type"]["developer"])

employee["permanent"] = False
employee["gender"] = "male"
del employee["age"]

print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(f"{key}: {value}")
