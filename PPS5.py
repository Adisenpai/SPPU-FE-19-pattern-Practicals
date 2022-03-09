""" 5. To check whether input number is Armstrong number or not. An Armstrong number is an
integer with three digits such that the sum of the cubes of its digits is equal to the number
itself. Ex. 371. """

T = int(input("Enter the number : "))

sum = 0

i = T

while i > 0:
    digit = i % 10
    sum += digit ** 3
    i = i // 10

if T == sum:
    print("The given number " + str(T) + " is an Armstrong number : ")
else:
    print("The given number " + str(T) + " is not an Armstrong number : ")

