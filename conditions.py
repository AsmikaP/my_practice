num1 = float(input("Enter a num 1"))
num2 = float(input("Enter a num 2"))

opr = input("Enter the operator")

if opr == "+":
    output = num1+num2

if opr == "-":
    output = num1-num2

if opr == "*":
    output = num1*num2

print("Your calculation is:", output)


if num1 > 3:
    print("num1 is greater than 3")

elif num1 == 3:
    print("num1 is equal to 3")

else:
    print("num1 is smaller than 3")