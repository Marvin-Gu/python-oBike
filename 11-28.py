a = 21
b = 10
c = 0

c = a + b
print("Line 1 - value of c is" , c)

c = a - b
print("Line 2 - value of c is" , c)

c = a * b
print("Line 3 - value of c is" , c)

c = a / b
print("Line 4 - value of c is" , c)

c = a % b
print("Line 5 - value of c is" , c)

a = 2
b = 3
c = a**b
print("Line 6 - value of c is" , c)


a = 10 
b = 5
c = a//b
print("Line 7 - value of c is" , c)

a = 21
b = 10 
c = 0

if ( a == b ):  
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equal to b")

if ( a!= b ):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")
'''
if ( a <> b ):
    print("Line 3 - a is not equal to b")
else:
    print("Line 3 - a is equal to b")
'''

if ( a < b ):
    print("Line 4 -a is less than b")
else:
    print("Line 4 - a is not less than b")

if ( a > b ):
    print("Line 5 -a is greater than b")
else:
    print("Line 5 - a is not greater than b")


a = 5 
b = 20 
if ( a <= b ):
    print("Line 7 - b is either greater than or equal to b")
else: 
    print("Line 7 - b is neither greater than nor equal to b") 

a = 21 
b = 10 
c = 0
c = a + b 
print("Line 1 - value of c is" , c)

c += a 
print("Line 2 value of c is" , c)

c *= a 
print("Line 3 value of c is" , c)

c /= a
print("Line 4 value of c is" , c)

c = 2 
c %= a
print("Line 5 value of c is" , c)

c **=a
print("Line 6 value of c is" , c)

c //= a
print("Line 7 value of c is" , c)
