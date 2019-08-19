"""
myName = 'taeyoon'  # global variable

변수를 정의할 때 함수 내에서 전역 변수에 접근하려고

# 1. when a variable is defined inside a function:

def print_name():
    myName = 'hyunho'
    print('the name inside the function is', myName)


print_name()
result: 'the name inside the function is hyunho'
print('outside the function the name is', myName)  

"""
# ---------------------------------------------------------------------------------------------------------------------------

# 2. when you want a variable to be overriden by another value, you need to use keyword 'global' in front of the variable name
# Then, you assign a new value to the variable.

myName = 'taeyoon'  # global variable


def print_name():
    global myName
    myName = "cheolsu"
    print('the name inside the function is', myName)


print_name()
print('outside the function the name is', myName)  # this will return error
