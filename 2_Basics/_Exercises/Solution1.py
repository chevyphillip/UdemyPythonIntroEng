"""Exercise 1:
1.)
Write code that chekcs the integer **number**
 The number is greater than 10 or less than 0:
    if True: print "True" in the console
    if not True: print "False" in the console

2.)
Write code that takes two floats x, y and computes:
- x*x + x*y + y*y
"""

# exercise1
number = 8

if number > 10 or number < 0:  # noqa: PLR2004
    print("True")
else:
    print("False")

# exercise2

x = 3.0
y = 2.0

result = x * x + x * y + y * y
print(result)
