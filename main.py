def rectangle_area(a, b):
    return a * b


a = float(input("Enter a: "))
b = float(input("Enter b: "))

area = rectangle_area(a, b)
print("Area: ", area)

"""
The issue is that input() in Python always returns a string, and you’re trying to multiply two strings (a * b), which causes the error.

✅ Fix: Convert the inputs to numbers (either int or float) before doing the multiplication.
Explanation:

input() → returns a string (e.g. "5")

float(input(...)) → converts it to a number (e.g. 5.0)

Then a * b correctly performs numeric multiplication.

If your inputs are always integers, you could also use int() instead of float().

"""