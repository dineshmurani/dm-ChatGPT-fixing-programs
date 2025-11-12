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
"""
password = input("Enter new password: ")

# Check conditions
result = {
    "length": len(password) >= 8,
    "digits": any(char.isdigit() for char in password),
    "upper-case": any(char.isupper() for char in password)
}

print(result)
print(result.values())

# Determine strength
print("Strong Password" if all(result.values()) else "Weak Password")
