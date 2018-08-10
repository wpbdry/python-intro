# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest (a, b, c):
    if a >= b and a >= c:
        res = a
    if b >= a and b >= c:
        res = b
    if c >= a and c >= b:
        res = c
    return str(res) + ' is the biggest out of ' + str(a) + ', ' + str(b) + ', and ' + str(c)



print (biggest(3, 6, 9))
#>>> 9

print (biggest(6, 9, 3))
#>>> 9

print (biggest(9, 3, 6))
#>>> 9

print (biggest(3, 3, 9))
#>>> 9

print (biggest(9, 3, 9))
#>>> 9