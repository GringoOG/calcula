input1 = input("Write first number: ")
input2 = input("Choose the operator: + , - , * , / , // , %: ")
input3 = input("Write second number: ")

number1 = float(input1)
operator = str(input2)
number2 = float(input3)

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    print(number1/number2)
elif operator == "//":
    print(number1//number2)
elif operator == "%":
    print(number1%number2)
else:
    print("Invalid operator")


