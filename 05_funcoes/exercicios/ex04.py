"""
4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""


def inverso_string(string):
    rstring = ''
    index = len(string)
    while index > 0:
        rstring += string[index - 1]
        index = index - 1
    return rstring


print(inverso_string('1234abcd'))