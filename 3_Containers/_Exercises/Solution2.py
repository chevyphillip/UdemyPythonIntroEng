"""Exercise 2:
1.)
Write code that uses a list of integer and one integer number "a".
There you should print the index where the number is present in the list.

2.)
Write code that takes two integers (x, y) computes the following:
Sum up all integer numbers from x (inclusive) to y (non-inclusive)
with a step width of 2.
"""

# exercise1
lst = [1, 2, 3]
a = 3

if a in lst:
    print(lst.index(a))
else:
    print("Not present at all.")


# exercise2
x = 2
y = 10

result = 0
for i in range(x, y, 2):
    result += i
print(result)
