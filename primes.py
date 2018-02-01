# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)

# These functions will ask you for your number ranges, and assign them to 'x1' and 'x2'
x1 = raw_input('smallest number to check: ')
x2 = raw_input('largest number to check: ')

# This line will print your two numbers out
print x1, x2

""" Text enclosed in triple quotes is also a comment.
This code should find and output all prime numbers between (and including) the numbers entered initially.
If no prime numbers are found in that range, it should print a statement to the user.
Now we end the comment with triple quotes."""

# The rest is up to you'
x1=eval(x1)
x2=eval(x2)
p="is prime"
for A in range(x1,x2):
    p="is prime"
    if A < 2:
        print false
    if A > 2:
        for i in range(2,A-1):
            if A % i == 0:
                print(A,"not prime")
                p="not prime"
                break
        if p=="is prime":
            print(A,"is prime")
