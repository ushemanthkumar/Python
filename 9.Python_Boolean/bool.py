# Boolean Values:-

print(10 > 9)
print(10 >= 20)

# using if conditions:-

a = 12
b = 34

if b < a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables:-

x="Vasco Da Gama"
y=5197

print(bool(x))
print(bool(y))

# Most Values are True and False:-

print(bool("VASCO DA GAMA"))   # Any string is true except empty string
print(bool(6930))  # Any number is true except 0
print(bool(["argumente","documents","instances"]))  # Any list, tuple, set, and dict is true except empty


# Values are False:-
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Function can return a boolean:-

def myfunction():
    return True
if myfunction():
    print("YES")
else:
    print("NO") 