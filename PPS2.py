""" 2. To accept an object mass in kilograms and velocity in meters per second and display its
momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is
its velocity. """ 

m = int(input("Enter mass of object in kgs : "))
v = int(input("Enter velocity of an object m/s : "))

# Momentum, p = mv
momentum = m * v

# Mass-Energy Equivalence, E = mc² (c is velocity)
MEeq = m * ( v ** 2)

print("object momentum is : ", momentum)
print("Mass-Energy Equivalence : ", MEeq)
