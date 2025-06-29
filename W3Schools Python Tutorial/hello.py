#I want to make a simple identity program#
first_name=input("What is your name? ")
last_name=input
gender=input("Are you a man (m) or a woman (w)? ")
last_name = input("What is your last name? ")
if gender == "m":
    print(f"Hello Mr. {first_name} {last_name}!")
elif gender == "w":
    print(f"Hello Ms. {first_name} {last_name}!")
else:
    print(f"Hello {first_name} {last_name}!")