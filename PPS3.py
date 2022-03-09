""" 3. To accept N numbers from user. Compute and display maximum in list, minimum in list,
sum and average of numbers. """

n = int(input("Enter total number of elements in the list : "))

list = []

# for loop to accept the numbers into the list.
for i in range(n):
    a = int(input("Enter the numbers : "))
    list.append(a)

print(list)

# max() function to find out the maximum value in the list.
maximum_no = max(list)

# min() function to find out the minimum value in the list.
minimum_no = min(list)

# sum() function to find the addition of all the values in the list.
sum_list = sum(list)

# Defining the average() function to find the average of all the values in the list.
# Calling the sum() function.
# Using len() function to find the total number of elements in the list.
def average(list):
    return sum_list / len(list)

# calling the average() function.
average_list = average(list)

print(maximum_no)
print(minimum_no)
print(sum_list)
print(average_list)


