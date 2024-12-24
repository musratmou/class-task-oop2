
def fun():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    result = (lambda a, b: a**2 + b**2 + 2 * a * b)(a, b)
    return result

print(f"The result is {fun()}")
