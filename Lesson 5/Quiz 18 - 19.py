# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
    l = name[0]
    if l == 'D' or l == 'd' or l == 'N' or l == 'n':
        return name + ' is your friend.'
    else:
        return str(name) + ' is not your friend.'






print (is_friend('Diane'))
#>>> True

print (is_friend('Fred'))
#>>> False

print (is_friend('daniel'))

print (is_friend('nadiene'))

print(is_friend('Naddie'))