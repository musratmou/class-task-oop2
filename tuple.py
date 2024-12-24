a = (1, 3, 5, 7, 4)

sum_odds = sum(x for x in a if x % 2 != 0)
sum_evens = sum(x for x in a if x % 2 == 0)
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)

a = a + (2, 4, 6)

a_list = list(a)
a_list.insert(2, 400)
a = tuple(a_list)

a = a[:-1]

sliced_tuple = a[-4:-1]

for num in a:
    if num == 5:
        continue
    print(num)

print(f"Sum of odd numbers: {sum_odds}")
print(f"Sum of even numbers: {sum_evens}")
print(f"Count of odd numbers: {odd_count}")
print(f"Count of even numbers: {even_count}")
print(f"Sliced tuple: {sliced_tuple}")
print(f"Final tuple: {a}")
