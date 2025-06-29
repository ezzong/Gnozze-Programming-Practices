# Strings
# Strings are series of character/s inside quotes

"""
# Changing the case of the string using .title method
name = "kenny omega"
print(name.title())

# Adding upper case and lower case method for variations
print(name.upper())
print(name.lower())

# Using variables in strings
first_name = "bryan"
last_name = "danielson"
full_name = f"{first_name} {last_name}"
print(full_name)

# Using f-string to compose message
first_name = "kota"
last_name = "ibushi"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Assigning the f-string to a shorter variable
message = f"Hello, {full_name.title()}!"
print(message)

# Adding tab to text
print("\tKenny Omega")

# Adding tabs and new lines to series of strings
print("Wrestlers:\n\tKenny Omega\n\tKota Ibushi\n\tKazuchika Okada")

# Removing whitespace: strip for both, lstrip/rstrip for each side
wrestler = "  kenny omega "
wrestler = wrestler.strip()
print(wrestler)

# Removing prefix
title = "the bout machine"
title = title.removeprefix("the ")
print(title)

# Example of syntax error with quotes
message = 'canada's iwgp champion'

# Practice
# Use a variable for a person name
name = "kenny"
print(f"Hi, {name}!")

# Print it in various cases
print(name.lower())
print(name.upper())
print(name.title())

# Print it with working quote
print(f'{name.title()} said "I am the greatest bout machine!"')

# Print with separate variables
name = "kenny omega"
message = " is the best wrestler in the world, of course."
print(f"{name.title()}{message}")

# Stripping whitespaces
print("Best Wrestlers:\n\tKenny Omega \n\t Kota Ibushi\n\t Kazuchika Okada ")
message = "Best Wrestlers:\n\tKenny Omega \n\t Kota Ibushi\n\t Kazuchika Okada "
print(message.strip())
"""

# Removing file extension using .removesuffix
filename = "AEW.pdf"
print(filename.removesuffix(".pdf"))


