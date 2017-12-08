# Basic list creation, usage
bicycles = ['trek', 'cannondale', 'mongoose', 'huffy'] # Create the list and prepopulate it with some values
print(bicycles)    # Prints [trek, cannondale, mongoose, huffy]
print(bicycles[0])  # Prints trek, the first item in the list as the the lists are zero indexed
print(bicycles[-1]) # Prints the last item in the list, huffy
print(bicycles[1].upper())  # Prints CANNONDALE, 2nd item in uppercase
bicycles[3] = 'specialized' # Changes the 4th item from huffy to specialized
bicycles.append('schwinn')  # Adds a new item at the end of the list, "schwinn" in this case
bicycles.insert(1, 'murray')  # Adds murray to the list in position 1, shifts everything to the right to fit it in. It does not overwrite anything.
print(bicycles)

# Pop vs del vs remove - Use del if you just want to remove it, use pop if you need to use it and remove it. Use remove if you know the value and not the position.
print("Deleting item at position 3:")
del bicycles[3] # Removes 'mongoose' which was in position 3 (4th item). Use del if you know the position.
print(bicycles)
print('Pop that sucker off there:')
popped_bicycle = bicycles.pop() # Pop removes the last item from the list if no parameters are given to the pop function and also returns that value so you can save it to a variable at the same time.
print('Popped: ', popped_bicycle)
print(bicycles)
print(bicycles.pop(2)) # Pop the item at position 2 and print it.

bicycles.remove('murray') # Search for and remove "cannonedale". Note that it only removes the first occurance. Use a loop if you need to remove others as well.
print(bicycles)


# Build a new list, this is very common since you don't know all of the data that will be added generally
components = [] # Create the empty list
components.append('resistor')   # Add resistor to the list, it'll be at position 0 since it's first. Append is a function so use ()
components.append('capacitor')  # Add another
components.append('transistor') # And another
print(components)   # Print the list, returns [resistor, capacitor, transistor]

# 3.1 Names
print('\n3.1 Names')
names = ['Kelly', 'Wendy', 'Corbin']
print(names[0])
print(names[1])
print(names[2])

# 3.2 Greetings
print('\n3.2 Greetings')
message = " is my friend."
print(names[0].title() + message)
print(names[1].title() + message)
print(names[2].title() + message)

# 3.3 Your Own list
print('\n3.3 Your Own List')
cars = ['lambo', 'ferrari', 'tesla', 'maserrati']
message1 = "I will own a "
message2 = " one day."
print(message1 + cars[0].title() + message2)
print(message1 + cars[1].title() + message2)
print(message1 + cars[2].title() + message2)
print(message1 + cars[-1].title() + message2)

# 3.4 Guest list
print('\n3.4 Guest List')
guests = ['Wendy', 'Corbin', 'Jon', 'Granny']
message = "I would love to have dinner with you, "
print(message + guests[0] + ".")
print(message + guests[1] + ".")
print(message + guests[2] + ".")
print(message + guests[3] + ".")

# 3.5 Changing Guest List
print('\n3.5 Changing Guest List')
print(guests[2]  + ' can\'t make it.')
guests[2] = 'Pa'
print(message + guests[0] + ".")
print(message + guests[1] + ".")
print(message + guests[2] + ".")
print(message + guests[3] + ".")

# 3.6 More Guests
print('\n3.6 More Guests')
print('More seats have become available!')
guests.insert(0, 'Bubba')
guests.insert(2, 'Mom')
guests.append('Dad')
print(message + guests[0] + ".")
print(message + guests[1] + ".")
print(message + guests[2] + ".")
print(message + guests[3] + ".")
print(message + guests[4] + ".")
print(message + guests[5] + ".")
print(message + guests[6] + ".")

# 3.7 Shrinking Guest List
print('\n3.7 Shrinking Guest List')
print("Unfortunately the table didn't arrive, only have room for 2 guests now")
message = "I'm sorry but the table didn't arrive, maybe next time "
print(message + guests.pop() + ".")
print(message + guests.pop() + ".")
print(message + guests.pop() + ".")
print(message + guests.pop() + ".")
print(message + guests.pop() + ".")
print("You're still invited " + guests[0])
print("You're still invited " + guests[1])
del guests[1]  # Gotta delete backwards or delete 0 multiple times as they move into that slot
del guests[0]
print(guests)
