🧮 Height Converter and Slide Eligibility Program
📘 Overview

This program allows users to enter their height in feet and inches, automatically converts it to meters, and then determines whether the user (a child, in this context) is tall enough to use a slide.

It demonstrates simple string manipulation, type conversion, and conditional logic in Python.

🧱 Features

Converts height from feet and inches to meters

Performs input validation via string splitting and conversion

Evaluates a height condition to determine slide eligibility

Provides user-friendly messages as output

🧩 Function Reference
convert(feet_inches)

Description:
Converts a height value expressed in feet and inches (as a single string) into meters.

Parameters:

feet_inches (str): A string containing two numeric values separated by a space, representing feet and inches respectively.
Example: "5 7" for 5 feet 7 inches.

Returns:

float: The equivalent height in meters.

Conversion Formula:

meters
=
(
feet
×
0.3048
)
+
(
inches
×
0.0254
)
meters=(feet×0.3048)+(inches×0.0254)

Example Usage:

height_m = convert("5 7")
print(height_m)  # Output: 1.7018

⚙️ Program Flow

User Input:
The program prompts the user to enter their height in the format "feet inches".
Example:

Enter feet and inches: 4 11


Conversion:
The convert() function splits the input and converts both values into meters.

Decision Making:

If the converted height is less than 1 meter, the program outputs:

Kid is too small.


Otherwise, it outputs:

Kid can use the slide.

💻 Full Code Example
def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")
result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

🧪 Example Runs

Example 1:

Enter feet and inches: 2 6
Kid is too small.


Example 2:

Enter feet and inches: 4 0
Kid can use the slide.

🧠 Notes

Input must contain two numeric values separated by a space.
Example: "5 8" ✅     "5" ❌     "five eight" ❌

The conversion constants used are based on standard metric relationships:

1 foot = 0.3048 meters

1 inch = 0.0254 meters

🏁 Conclusion

This simple height converter illustrates:

String parsing and type conversion

Arithmetic operations for unit conversion

Basic conditional logic in Python

It can be expanded to include input validation, exception handling, or GUI/Flask interfaces for enhanced usability.