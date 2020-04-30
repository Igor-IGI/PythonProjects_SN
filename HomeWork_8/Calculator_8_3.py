first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

arithmetic_operation = input("Choose operation +,-,*,/: ")

if arithmetic_operation == "+":
    print(first_number + second_number)
elif arithmetic_operation == "-":
    print(first_number - second_number)
elif arithmetic_operation == "*":
    print(first_number * second_number)
elif arithmetic_operation == "/":
    print(first_number / second_number)
else:
    print("You chose invalid operation")