# PYTHON OPERATORS........

#Python Arithmetic operators:--
x = 4
y = 2
print(x + y)        #Addition..
print(x - y)        #Subtraction..
print(x * y)        #Multiplication..
print(x / y)        #Division..
print(x % y)        #Modulus..
print(x ** y)       #Exponentiation..
print(x // y)       #Floor division..

#Python Assignment operators:--
a = 3
print(a)            #Simple Assignment..
a += 4
print(a)            #Add and Assign..
a -= 10
print(a)            #Subtract and Assign..
a *= 2
print(a)            #Multiply and Assign..
a /= 3
print(a)            #Divide and Assign..
a %= 3
print(a)            #Modulo and Assign..

b =3
b &= 2
print(b)            #Bitwise AND and Assign..
b |= 7
print(b)            #Bitwise OR and Assign..
b ^= 5
print(b)            #Bitwise XOR and Assign..
b <<= 1
print(b)            #Left Shift and Assign..
b >>= 2
print(b)            #Right Shift and Assign..

#Python Comparison Operators:--
h = 12
k = 13
print(h == k)       #Equal..
print(h != k)       #Not Equal..
print(h > k)        #Greater than..
print(h < k)        #less than..
print(h <= k)       #less than are equal to..
print(h >= k)       #Greater than are equal to..

#Python Logical operators:--
r = 56
print(r > 34 and r < 78)
print(r < 34 and r > 78)        #logical "and" operation..

t = 56
print(t > 34 or t < 78)
print(t > 34 or t > 78) 
print(t < 34 or t < 78)
print(t < 34 or t > 78)         #logical "or" operation..

z = 12
print(not(z > 11 and z < 34))
print(not(z < 11 or z > 34))    #logical "not" operation..

#Python Identity Operators:--
l = ['car','van','bus','bike']
k = ['car','van','bus','bike']
j = l
print(l is k)
print(l is j)
print(k is j)
print(l is not k)
print(l is not j)
print(k is not j)       # is and is not..

#Python Membership Operators:--
c = ['car','van','bike']
print('car' in c)
print('bus' in c)
print('bus' not in c)
print('bike' not in c)      # in and not in..

#Python Bitwise Operators:--
Q = 2
W = 3
print(Q & W)        #AND..
print(Q | W)        #OR..
print(Q ^ W)        #XOR..
print(~Q)           #NOT..
print(~W)
print(Q << 2)       #ZERO FILL LEFT SIDE..
print(W >> 1)       #SIGNED RIGHT SIDE..
