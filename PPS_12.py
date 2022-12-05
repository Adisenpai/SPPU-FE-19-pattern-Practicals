"""" 12. To accept list of N integers and partition list into two sub lists even and odd numbers. """

x = list()
n = int(input("Number of elements in main list: "))
print("Enter the elements of first list:")
for i in range(int(n)):
    k = int(input())
    x.append(k)

def find_evenodd(x):
    even = []
    odd = []

    for i in x:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print("Sublist of even numbers:", even)
    print("Sublist of odd numbers: ", odd)


find_evenodd(x)