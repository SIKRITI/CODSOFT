print("Calculator")

num1 = float(input("Enter the first number of your choice: "))
num2 = float(input("Enter the second number of your choice: "))

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")

choice = int(input("\nEnter your choice from 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("The choice is invalid")
