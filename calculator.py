def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Subtraction")
print("2. Multiplication")
print("3. Division")

choice = input("Enter your choice (1, 2 or 3): ")

if choice == "1":
    print("Subtraction =", subtraction(num1, num2))

elif choice == "2":
    print("Multiplication =", multiplication(num1, num2))

elif choice == "3":
    print("Division =", division(num1, num2))

else:
    print("Invalid choice")