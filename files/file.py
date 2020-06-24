# Open files, read a file
"""file = open("text.txt", "r")
x = file.read()
print(x)"""

# Writing files
file = open("test.txt","w")
file.write("pink\n")
file.write("pink\n")
x = ["red", "blue", "green", "black"]

for item in x:  # Add elements from list to file
    file.write(item + "\n")
file.close()
"""file = open("test.txt", "r", encoding="utf-8")
read = file.read()
print(read)"""

# Append element
file = open("test.txt", "a")
file.write("pink")
file.close()

# Different methods
"""

r
r+

w
w+

a
a+

"""