import math
def Greet():
    print("Hello world")
def add_numbers():
    num1 = int(input("Enter the value of first number:"))
    num2 = int(input("Enter the value of second number:"))
    a = int(num1 + num2)
    print("The sum of", num1, "and", num2,"is",a)
def square_of_num():
    digit = (int(input("Enter the value of digit for squaring:")))
    result = digit * digit
    return result
def add_numbers2():
    num1 = int(input("Enter the value of first number:"))
    num2 = int(input("Enter the value of second number:"))
    a = int(num1 + num2)
    return a
def square_root():
    digit = (float(input("Enter the value of the digit want to square root:")))
    answer = math.sqrt(digit)
    return answer
def square_of_num(digit):
    result = digit * digit
    return result
def factorial(dig):
    # dig = int(input("Enter the value of integer:"))
    if dig==1:
        return 1
    else:
        return (dig * factorial(dig-1))
    
# Greet()
# add_numbers()
# a = square_of_num()
# print(a)
# for i in [1,2,3]:
#     x = square_of_num(i)
#     print("The square of",i,"is:",x)
# add = add_numbers2()
# print(add)
# root = square_root()
# print(root)
# a = factorial(3)
print("The factorial of the number is:",factorial(5))






