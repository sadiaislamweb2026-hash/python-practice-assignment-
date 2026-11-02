name = input("Enter your name: ")
age = int(input("Enter your age: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"\nHello, {name}!")
print(f"Your age is {age}.")

print(f"Addition: {addition:g}")
print(f"Subtraction: {subtraction:g}")
print(f"Multiplication: {multiplication:g}")

if num2 != 0:
    division = num1 / num2
    print(f"Division: {division}")
else:
    print("Division: Cannot divide by zero.")
