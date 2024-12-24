arr = [10, 5, 15, 20]

try:
    divisor = int(input("Enter a divisor: "))
    index = int(input("Enter an index (0 to 3): "))

    # Handling division
    result = arr[index] / divisor
    print(f"Result of division: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except IndexError:
    print("Error: Index out of range. Please select an index between 0 and 3.")
finally:
    print("Execution completed.")
