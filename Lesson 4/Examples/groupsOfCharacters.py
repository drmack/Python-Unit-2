"""
This program shows how index values are assigned and utilized to isolate
multiple characters in a string.
"""

# indexes:             0   1   2   3   4   5
#                      h   e   l   l   o   !
# negative indices:    -6  -5  -4  -3  -2  -1
my_string = "hello!"

print "my_string[1:3] is " + my_string[1:3]
print "my_string[1:] is " + my_string[1:]
print "my_string[:3] is " + my_string[:3]