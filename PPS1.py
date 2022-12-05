""" 1. To calculate salary of an employee given his basic pay (take as input from user).
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of
basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary
payable after deductions. """

b = int(input("enter your basic  pay : "))
hra = b * 0.1
ta = b * 0.05
gross = b + hra + ta
tax = gross * 0.02
net = gross - tax

print("your net salary is :", net)
