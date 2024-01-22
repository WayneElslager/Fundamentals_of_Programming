#Question 1: Take an input string from the user and create a new string with the first, middle, and last characters of the input string

user_string = input("Please enter a string: ")
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

# To get the middle character, find length and index of middle character
str_length = len(user_string)
mid_index = int(str_length/2) # since indices can only be integers

mid_char = user_string[mid_index] # To access the char at mid index
result_str = first_char + mid_char + last_char
print(result_str)