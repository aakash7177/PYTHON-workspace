"""
input() in Python is a function that **takes user input from the keyboard as a string**.

--------------------------------------------------------------------------------------------

### ✅ Simple Example:

python
name = input("Enter your name: ")
print("Hello, " + name)


**What happens:**

1. Program shows: `Enter your name: `
2. User types something (e.g., `Aakash`)
3. Program outputs: `Hello, Aakash`

--------------------------------------------------

### Important points:

* The result of `input()` is always a **string**.

👉 Example:

python
age = input("Enter your age: ")
print(type(age))


Even if you type `25`, the type will be `<class 'str'>`.

------------------------------------------------------------------

### Converting input to integer:

python
age = int(input("Enter your age: "))
print("Next year, you'll be", age + 1)


If you don't convert to `int`, `age + 1` would concatenate strings (e.g., "25" + 1 → error).

------------------------------------------------------------------------------------------------

### Quick recap:

* `input(prompt)` → shows `prompt`, waits for user input.
* Always returns a string.
* Use `int()`, `float()`, etc., to convert if needed.

"""

input("what is your name = ")
print("your name is " + input("what is your name again? = ") + ". Am i right?")