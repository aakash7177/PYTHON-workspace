print(7 / 2 ) # this will return 3.5
print(7 // 2 ) # this will return 3 , becauuse // function remove all the value after decimal.
# but what if we want to round off an number.

# round() function
"""
- The round() function in Python is used to round a number to a specified number of decimal places.

✅ Syntax:
round(number, digits)

- number: The number you want to round.
- digits (optional): The number of decimal places to round to. If omitted, it rounds to the nearest integer.



1) Round to nearest integer:
print(round(5.7))    # Output: 6
print(round(5.3))    # Output: 5
print(round(-2.5))   # Output: -2 (Python rounds towards even numbers in tie cases)

2) Round to specific decimal places:
print(round(3.14159, 2))    # Output: 3.14
print(round(2.71828, 3))    # Output: 2.718

NOTE - In case of tie-breaking (e.g., round(2.5)), Python uses round-half-to-even (bankers rounding):
round(2.5)  # Output: 2
round(3.5)  # Output: 4

"""
# end of notees 1

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi , 0))
print(round(bmi , 1))
print(round(bmi , 2))

"""
NOTE = 0 daaloge tab number ko round off krke float me answer de dega.
     = 1 pe decimal ke 1 digit baad round off krega 2 pe 2 digit badd.
"""




# F-string
"""
- F-string in Python is a way to embed expressions inside string literals for easy and readable string formatting.

✅ Syntax:
f"Some text {expression} more text"

- Prefix the string with f or F.
- Put any Python expression inside {} and it will be evaluated and inserted in the string.

✅ Example :
name = "Himmel"
age = 20
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Himmel and I am 20 years old.

"""