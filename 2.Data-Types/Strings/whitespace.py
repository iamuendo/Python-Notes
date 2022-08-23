# Adding whitespace
# Types of whitespaces
# \n - displays values on a new line
# \t - to add tab spaces

favourites = "These are my favourite langauges:\n\t-Python\n\t-Javascript\n\t-R"
print("Adding whitespaces-\n" + favourites)

# Removing whitespaces
# rstrip() - strips whitespaces on the right side of the string
# lstrip() - strips whitespaces on the left side of the string
# strip() - strips whitespaces from both the right & left side of the string
username = 'Pythonuser001   '
bio = ' I love python programming'
fullname = '  Isaac Muendo  '
# Before removing whitespaces
print(f"{username}\n{bio}\n{fullname}\n")

#After removing whitespaces
print(f"{username.rstrip()}\n{bio.lstrip()}\n{fullname.strip()}\n")