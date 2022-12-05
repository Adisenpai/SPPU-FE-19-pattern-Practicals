""" To accept two numbers from user and compute smallest divisor and Greatest Common
Divisor of these two numbers. """

""" Smallest divisor of two numbers can be considered as 1. """

a = int(input('Enter the first number : '))
b = int(input('Enter the second number : '))

# Here we will first compare which number is the smaller one.
if a > b:
    minval = b
else:
    minval = a

# There are 2 possibilities,
# 1. The smaller number is the GCD.
# 2. The number below the smaller number is GCD.
# For that, We will use for loop to iterate until the smaller number is reached.
for i in range(1, minval + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print(f"The gcd of the given two numbers is : {hcf}")

# Alternative method
#
# # GCD of two numbers
# # Defining a function named gcd()
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# print("The gcd of a and b is : ", end="")
# print(gcd(a, b))
#

# LCM of two numbers
if a > b:
    maxval = a
else:
    maxval = b

while(True):
    if maxval % a == 0 and maxval % b == 0:
        print(f"The lcm of the given two numbers is : {maxval}")
        break
    maxval = maxval + 1


