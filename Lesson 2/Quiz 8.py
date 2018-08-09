# Assume text is a variable that holds a string.
# Write Python code that prints out the position of the second occurrence of 'zip' in text,
# or -1 if it does not occur at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped"

# ENTER CODE BELOW HERE

f_pos = text.find('zip') # first occurence of 'zip
s_pos = text.find('zip', f_pos + 1) # second occurence of 'zip'
print ('''The second occurence of "zip" is found at position ''' + str(s_pos)
        + ''' in the string "''' + text + '''".''')
