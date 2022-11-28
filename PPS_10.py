""" 10. To input binary number from user and convert it into decimal number. """

# Taking binary input
binary = input("Enter a binary number:")

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)
    
# Calling the function
BinaryToDecimal(binary)

