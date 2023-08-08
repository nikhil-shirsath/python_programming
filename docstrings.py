# docstrings are special type of function which specifies the feature
# of our user difined function.
# Its must to write it at the first line of the functions defination.

# note : in the docstring we can use multiple lines as we want which we cant do with strings


# To craate docstring we writes the text inside the three double strings.

# """ here we writes docstring"""  

# this message is visible for the programmer during development.

def sum(first, second):
    """This function takes two arguments and returns sum of the 
    two numbers which is simply an addition operation."""
    return first+second
print(sum(11,22))
