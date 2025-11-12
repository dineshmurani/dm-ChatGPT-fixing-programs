# password = input("Enter new password: ")
#
# result = {}
#
# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False
#
# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
#
# result["digits"] = digit
#
# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
#
# result["upper-case"] = uppercase
#
#
# print(result)
# print(result.values())
#
# if all(result.values()):
#     print("Strong Password")
# else:
#     print("Weak Password")
"""
More elegant code from chatGPT
Improvements made:

Used any() instead of loops for digits and uppercase checks.

Removed unnecessary boolean variables.

Used a dictionary literal directly for concise assignment.

Used a ternary operator for the final print.

If you want, I can make it even fancier by turning it into a reusable function that also checks for symbols and lowercase letters.
"""
# password = input("Enter new password: ")
#
# # Check conditions
# result = {
#     "length": len(password) >= 8,
#     "digits": any(char.isdigit() for char in password),
#     "upper-case": any(char.isupper() for char in password)
# }
#
# print(result)
# print(result.values())
#
# # Determine strength
# print("Strong Password" if all(result.values()) else "Weak Password")
"""
more elegant by chatGPT
"""
# import string
#
#
# def check_password_strength(password: str) -> dict:
#     """Check password strength and return a dictionary of criteria."""
#     symbols = set(string.punctuation)
#
#     result = {
#         "length": len(password) >= 8,
#         "digits": any(c.isdigit() for c in password),
#         "upper-case": any(c.isupper() for c in password),
#         "lower-case": any(c.islower() for c in password),
#         "symbols": any(c in symbols for c in password)
#     }
#
#     return result
#
#
# # Example usage
# password = input("Enter new password: ")
# strength = check_password_strength(password)
#
# print(strength)
# print(strength.values())
# print("Strong Password" if all(strength.values()) else "Weak Password")

"""
more elegant code with password checker
"""
import string

def check_password(password: str) -> dict:
    """Check password criteria and return a dictionary of booleans."""
    symbols = set(string.punctuation)
    return {
        "length": len(password) >= 8,
        "digits": any(c.isdigit() for c in password),
        "upper-case": any(c.isupper() for c in password),
        "lower-case": any(c.islower() for c in password),
        "symbols": any(c in symbols for c in password)
    }

def password_feedback(strength: dict) -> None:
    """Print user-friendly feedback based on password strength."""
    if all(strength.values()):
        print("✅ Strong Password")
    else:
        print("❌ Weak Password. Improve by adding:")
        for criterion, passed in strength.items():
            if not passed:
                messages = {
                    "length": "- At least 8 characters",
                    "digits": "- At least one digit",
                    "upper-case": "- At least one uppercase letter",
                    "lower-case": "- At least one lowercase letter",
                    "symbols": "- At least one special symbol (!@#$...)"
                }
                print(messages[criterion])

# Example usage
password = input("Enter new password: ")
strength = check_password(password)

print(strength)         # Show the detailed boolean dictionary
password_feedback(strength)


