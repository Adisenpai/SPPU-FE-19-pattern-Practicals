""" To accept an object mass in kilograms and velocity in meters per second and display its
momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is
its velocity. """ 

m = int(input("Enter mass of object in kgs :"))

v = int(input("Enter velocity of an object m/s :"))

# Mass-Energy Equivalence, E = mc²
MEeq = m * ( v ** 2)

# Momentum, p = mv
momentum = m * v

print("Mass-Energy Equivalence :", MEeq)
print("object momentum is :", momentum)