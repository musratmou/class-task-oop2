a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

print(a)
print(b)
print(len(a), len(b))
print(type(a), type(b))

a.add(10)
a.remove(8)

union = a.union(b)
intersection = a.intersection(b)
difference = a.difference(b)
symmetric_difference = a.symmetric_difference(b)

issubset_result = a.issubset(b)

a = a.union([2, 3, 4])

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")
print(f"Symmetric Difference: {symmetric_difference}")
print(f"Issubset: {issubset_result}")
print(f"Updated a: {a}")
