# Input Method
# In Python 2 the method input return number
# In python 3 the method input return string


def div(a, b):
    if b == 0:
        return print("This is not possible, are you mad?")
    else:
        c = a/b
        return print(c)


a = input("Enter the value: ")
b = input("Enter the second value: ")
div(int(a),int(b))