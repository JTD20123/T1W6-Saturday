#Simple calculator using if-else statements

# Get user input

num1 = float(input("Enter first number"))
operation = (input("Enter operation + - * /"))
num2 = float(input("Enter Second number"))

# Perform calculation using if-else statements

if operation == '+':
    result = num1 = num2    
elif operation == '-':
    result = num1 = num2    
elif operation == '*':
    result = num1 = num2    
elif operation == '/':
    result = num1 = num2    
else:
    result = "Error! invalid Operation"

print(f"The result is:{result}")
