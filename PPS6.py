""" To simulate simple calculator that performs basic tasks such as addition, subtraction,
multiplication and division with special operations like computing x^y
and x!. """

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

print("Operations: +, -, *, /, x^y, x!")
chose = input("Chose the operation to be performed : ")

if chose == "+":
 print(x, "+", y, "=", x + y)
elif chose == "-":
 print(x, "-", y, "=", x - y)
elif chose == "*":
 print(x, "*", y, "=", x * y)
elif chose == "/":
 print(x, "/", y, "=", x / y)
elif chose == "x^y":
 print(x, "^", y, "=", x ** y)
elif chose == "x!":
 print(x, "!=", y, "=", x != y)
else:
 print("Invalid input")



