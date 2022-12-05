""" To accept the number and Compute a) square root of number, b) Square of number, c)
Cube of number d) check for prime, d) factorial of number e) prime factors """

a = int(input("Enter the number : "))
square_root = a ** 0.5
square = a ** 2
cube = a ** 3

print('The square root of ', a, "is", square_root, ".")
print('The square of ', a, "is", square, ".")
print('The cube of ', a, "is", cube, ".")

# Logic to check whether a given number is prime or not.
for i in range(2, a):
    # Checking if the number is divisible by any other numbers excluding 1 and the number itself.
    if a % i == 0:
        print("The given number ", a, "is not a prime number.")
    break
else:
    print("The given number ", a, "is a prime number.")


# Logic to find the factorial of a number.
fact_num = 1
# Checking if the input is valid or not.
if a < 0:
    print("Factorial does not exist for negative numbers.")
elif a == 0:
    print("The factorial of 0 is 1.")
# Multiplying each number till the given number reached.
else:
    for i in range(1, a + 1):
        fact_num = fact_num * i
    print("The factorial of", a, "is", fact_num, ".")


# Logic for prime factors
prime_fact = []
divisor = 2
while divisor <= a:
    # Checking each time if a divisor is a factor of 'a'.
    if a % divisor == 0:
        prime_fact.append(divisor)
        a = a / divisor
    else:
        #
        divisor += 1

print("The prime factors of the given number are ", prime_fact, ".")
