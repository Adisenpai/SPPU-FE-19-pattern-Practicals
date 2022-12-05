""" 5. To check whether input number is Armstrong number or not. An Armstrong number is an
integer with three digits such that the sum of the cubes of its digits is equal to the number
itself. Ex. 371. """

T = int(input("Enter the number : "))
sum = 0
i = T

# Using while loop to perform the desired operations on each digit.
while i > 0:
    # Following operation will give us the remainder which will be the last digit of the number.
    digit = i % 10
    # This step will add the cube of the digit to the sum.
    sum += digit ** 3
    # Finally this operation will store the quotient into i so that we can perform same operations on the next digits.
    i = i // 10

# Checking if the number is Armstrong number or not and printing the result.
if T == sum:
    print("The given number " + str(T) + " is an Armstrong number : ")
else:
    print("The given number " + str(T) + " is not an Armstrong number : ")

