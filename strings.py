'''
print("Hello World!")
# For variable names, do not use reserved keywords
# print(help("keywords"))

# Assign multiple variables with the same value simultaneously
a = b = c = 10  # works but not recommended
print(a,b,c)

# Expression vs statement
x = 47  # statement
y = 47 + 10  # expression



# TYPE CONVERSION
# Converting to int
print(int(10.24))
print(int(float("10.24")))

# Converting to str
print(str(20))
print(type(str(20)))


# STRINGS
# Can be created either by single, double or triple quotes
first_name = 'Jane'
print(first_name)

last_name = "Doe"
print(last_name)
address = "10 Main St"
print(address)
job1 = "Physician's Assistant"
print(job1)

#STRING FUNCTIONS
emp_name = "Jane Doe"
# len() -->returns the number of characters in a given string
print(len(emp_name))

#upper and lower --> these convert the string into corresponding cases
print(emp_name.upper())

# String concatenation
first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)

age = 24
print(first_name + ' ' + last_name + ': ' + str(age))

# String multiplication
print("Hello"*3)
# Can only add 2 strings and can only multiply a string with an int
'''

# Accessing string characters
emp_name = "Jane Doe"
print(emp_name[3])
# print(emp_name[8]) # throws index out of bounds error because the last char is at index 7

print(emp_name.index('n'))

