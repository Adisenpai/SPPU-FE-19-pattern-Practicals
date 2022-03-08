""" 3. To accept N numbers from user. Compute and display maximum in list, minimum in list,
sum and average of numbers. """

n = int(input("Enter total number of elements in the list :"))

list = []

for i in range(n):
    a = int(input("Enter the numbers :"))
    list.append(a)

print(list)

maximum_no = max(list)

minimum_no = min(list)

sum_list = sum(list)

def average(list):
    return sum_list / len(list)

average_list = average(list)

print(maximum_no)
print(minimum_no)
print(sum_list)
print(average_list)


