# Define a function to convert height in feet and inches to meters
def convert(feet_inches):
    # Split the input string into two parts: feet and inches
    parts = feet_inches.split(" ")

    # Convert the string parts to floating-point numbers
    feet = float(parts[0])
    inches = float(parts[1])

    # Convert feet to meters (1 foot = 0.3048 meters)
    # Convert inches to meters (1 inch = 0.0254 meters)
    meters = feet * 0.3048 + inches * 0.0254

    # Return the total height in meters
    return meters


# Ask the user to input their height in feet and inches (e.g., "5 7")
feet_inches = input("Enter feet and inches: ")

# Call the convert function to get the height in meters
result = convert(feet_inches)

# Check if the height is less than 1 meter
if result < 1:
    # If height is less than 1 meter, print a message
    print("Kid is too small.")
else:
    # If height is 1 meter or more, print a different message
    print("Kid can use the slide.")
