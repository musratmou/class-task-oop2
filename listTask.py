a = [1, 3, 5, 7, 4]
print(f"Element at a[-2]: {a[-2]}")
print(f"Element at a[2]: {a[2]}")

# Finding the length and type
length = len(a)
type = type(a)
print(f"Length of the list: {length}")
print(f"Type of the list: {type}")


a[-3] = 50

sliced_list = a[2:4]

print(a)
print(sliced_list)  

a[1] = 100  
a[2] = 200  

print(a)


# Remove the last element
a.pop()

# Remove the element at index 1
a.pop(1)

# Join a new list [2, 4, 6] with list a
a.extend([2, 4, 6])

# Copy all values of a to a new list b
b = a.copy()

# Sort the elements of b
b.sort()


for num in b:
    print(num)
    if num == 5:
        break


largest = max(a)

print(f"Largest number in a: {largest}")
