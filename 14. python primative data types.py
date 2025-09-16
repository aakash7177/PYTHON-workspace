# Subscripting :
# Subscripting means accessing individual elements from a sequence using square brackets [ ] and an index.


# start of notes 1
"""

### **Python String Indexing**

* Strings in Python are like lists of characters.
* Each character has an **index** starting from **0**.

#### Example:

```python
print("hello"[2])
```

👉 Output:

```
l
```

Explanation:

* `"hello"` is a string → `h (0), e (1), l (2), l (3), o (4)`
* `[2]` means: give me the character at index 2 → which is `"l"`

---

Negative indexing :
Negative indexing works too!
`"hello"[-1]` → `'o'` (last character)


"""
# end of notes 1


# Data types

"""
we have mostly 4 types of data ;-
a) string or str 
b) integer or int 
c) float
d) boolean or bool
"""

# A) string data type , str

"""
To make a data into string we have to use double qoutation "".
"""
print("123" + "345") # output = 123345
name = "aakash"
print(name) # output = aakash


# B) integer data type , int 

"""
- This data type can store whole number.
- using underscore _ between the number are ignored by the compiler.
"""
no_of_hand = 2
print(no_of_hand)
body_count1 = 43878957207
body_count2 = 43_878_957_207
print(body_count1)
print(body_count2)
print(123 + 345)

# C) float data type , Floating Point Number

"""
this data type can store numbers with decimal point.
"""
pi = 3.14
dick_size = 6.3
print(pi)
print(dick_size)

# D) boolean data type , bool

"""
- This data type can store only two value which is True & False.
- python is a case sensitive language so the 1st letter of True/False should be capital.
- using true/false instead of True/False can give you an error.
"""

want_sex = True
asexual = False