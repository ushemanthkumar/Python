x = 1000   # float
y = 28.988  # int
z = 66j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Get single random numbre ...
import random

print(random.randrange(1, 10))

# Get multiple random numbers ...

import random

for i in range(8):
    print(random.randrange(1,100))