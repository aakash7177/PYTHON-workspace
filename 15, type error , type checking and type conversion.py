# Type error 
"""
- We already know that len() function is used to find the lenght of string.
- Using anything else except string will give you an Type error.
"""
print(len("1234567"))
# print(len(1234567)) output = error 

# Type checking
"""
- Type() function is used to check the type of data , wheather it is string or integer or float or boolean.
- we have to used it with print function to print the type.
"""

dick_color = "brown"
print(type(dick_color))
dick_size = 6.3
print(type(dick_size))
testical = 2
print(type(testical))
have_sex = True
print(type(have_sex))


# Type conversion
"""
- using int() , float() , str() , bool() , we can convert one data type into another.
- same as type() function and len() function , they are used with different function.
"""


# pratice question-1 
"""
Q1) Make this code of line run without error.
   print("numbers od letters in your name: " + len(input("Enter your name = ")))
"""

print("numbers of letters in your name: " + len(input("Enter your name = ")))


# pratice question 2
"""
Q2) Write code to print the length of the string "datascience".
"""

# pratice question 3
"""
Q3) What happens if you try to run this code?
    print(len(98765))
"""

# pratice question 4
"""
Q4) Write code to check and print the data type of the following values:
    -"hello"
    -3.14
    -42
    -False
"""
