# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):

    if isinstance(n, int):
        i = n
        res = 1
        while i > 1:
            res = res * i
            i = i - 1
        return str(n) + '! = ' + str(res)
    else:
        return 'Factorial error: Please enter an integer'

print (factorial(4))
# >>> 24
print (factorial(5))
# >>> 120
print (factorial(6))
# >>> 720

print (factorial(42))

print (factorial(3.2))

