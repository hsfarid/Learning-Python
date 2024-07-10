#argument variable
# from sys import argv
# script, first, second, third = argv

# print("The script is called: ", script)
# print("The first variable is: ", first)
# print("The second variable is: ", second)
# print("The third variable is: ", third)

# script, user_name = argv
# prompt = "> "

# print(f"Hi {user_name}, I'm the {script} script.")
# print("i'd like to ask you a few questions!")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)
# print("Where do you live?")
# lives = input(prompt)
# print("What kind of computer do you have?")
# computer = input(prompt)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice!
# """)

#opening, writing and reading files
# from sys import argv

# #this unpacks and allows us to pass two argument variables
# script, filename = argv

# # this opens the file and returns an object 
# f = open(filename)
# print(f"Here's your file {filename}")
# # the read method reads the content of the file object 
# print(f.read())
# print(f.readline())

# print('Type the file name again')
# file_name_again = input("> ")
# txt_again = open(file_name_again)
# print(txt_again.read())
# f.close()
# txt_again.close

from sys import argv

script, file_name = argv

print(f"We're going to erase {file_name}")
print(f"If you don't want that, hit CTRL + C (^C)")
print("If you want that, hit RETURN.")
input("? ")

print("Opening the file....")
f = open(file_name, 'w')

print('Truncating the file. Goodbye.')
f.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
f.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally we close it.")
f.close()





