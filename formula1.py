def fun(a, b):
    return a**2 + b**2 + 2 * a * b


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

result = fun(a, b)
print(f"The result of a^2 + b^2 + 2ab is: {result}")
