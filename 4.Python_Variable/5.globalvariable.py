# global variable

# Variables that are created outside of a function  
# Global variables can be used by everyone, both inside of functions and outside.

x = "Footballer"

def myfunc():
  x = "Cricketer"
  print("M S Dhoni is " + x)

myfunc()

print("M S Dhoni is " + x)


# 2.

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "Cricketer"

myfunc()

print("M S Dhoni is " + x)

# 3.

x = "Footballer"

def myfunc():
  global x
  x = "Cricketer"

myfunc()

print("M S Dhoni is " + x)