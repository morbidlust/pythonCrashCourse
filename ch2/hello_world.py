# Define/set a variable and print it's output to the screen
# Note in Python2 the print function does not have (), Python3 requires print()
message = "Hello World Python"
print(message)

"""
Multiline comment
Set the variable and then print it using methods title() upper() and lower() which changes the case of the text when printing it
"""
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())

# Add some more text around the full name
message = "Hello " + full_name.title() + ", hope you have a good day."
print(message)

#Print with a tab first_name
print("\tPython Rulez!")

#Using the newline character this time
print("Languages:\nPython\nC\nPHP")

#Strip extra whitespace from the right side of a string
txt = "Strip this       "
print(txt.rstrip() + ". This should butt up against txt")

#Edit strip and remove the whitespace saved in the variable
txt = txt.rstrip()
print(txt)

#Remove whitespace from the left
txt = "        woa spaces         "
print(txt)
print(txt.lstrip())

#Remove whitespace from the left and right at the same time
print(txt.strip())

# You can't add (concat) strings and numbers. Convert the number to a string first or you'll get an error
age = 36
#    print("Happy birthday, you're now " + age)     # Will error as you can't add an int to a string
print("Happy birthday, you're now " + str(age))         # This works as str() converts the int 'age' to a string first
