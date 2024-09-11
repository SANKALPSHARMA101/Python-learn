import math
import tempConversion
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

def calcSomething(x):
    return 2* x**2  
def sum_of_3_multiplies(n):
    return n * 1 + n * 2 +  n * 3   
def multiply(a,b):
    print(a*b)
def check():
    a = input("Enter the value of first variable:")
    b = input("Enter the value of second variable:")
    c = input("Enter the value of third variable:")
# Defalut arguements
def simple_interest(principal, cc ,time = 2,rate = 0.10):
    return (principal*time*rate)/100
# Void functions
def greet():
    print("Hello")
def calculator(a,b):
    return a+b,a-b,a*b,a%b,a/b
# Passing an Immutable type value to a function
def myFunc1(a):
    print("Inside myFunc1()")
    var = int(input("Enter the value:"))
    print("Value recieved in 'a' as",a)
    a = a+2
    print("Value of a now changes to",a)
    print("Returning from myFunc1()")
# Passing a mutable type value to a function
def myFunc2(myList):
    print("Inside myFunc2()")
    print("List recieved in 'myList' as",myList)
    myList[0] += 2
    print("List within called fucntion, after changes:",myList)
    return
def myFunc3(myList):
    print("Inside myFunc3()")
    print("List recieved in 'myList' as",myList)
    myList.append(2)
    myList.extend([5,1])
    print("List after adding some elements:",myList)
    myList.remove(5)
    print("List within called fucntion, after changes:",myList)
    return
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
# print("The factorial of the number is:",factorial(5))
# print(calcSomething(2))
# print(sum_of_3_multiplies(7))
# multiply(3,6)
# p = 9
# multiply(3,p)
# multiply(p,p+1)   # POLYMORPHISM
# print(check())
# print("You entered 3 numerical value.")
# print(check())
# print("You entered one alphabetical and 2 numerical value.")
# print(check())
# print("You entered 3 alphabetical value.")
# print(simple_interest(12000,2)) # -->Legal
# print(simple_interest(rate = 0.12, principal = 5000, cc = 4))   # -->Legal
# print(simple_interest(cc = 4, rate = 0.12, principal = 5000))   # -->Legal
# print(simple_interest(5000, 3, rate = 0.05))    # -->Legal
# print(simple_interest(rate = 0.05, 5000, 3))  --> Illegal
# print(simple_interest(5000, principal = 300, cc = 2)) --> Illegal
# print(simple_interest(500, time = 2, rate = 0.05))    --> Illegal
# greet()
# print(calculator(2,4))
# num = 3
# print("Calling myFunc1() by passing 'num' with value",num)
# myFunc1(num)
# print("Back from myFunc1(). Value of num now is")
# List1 = [2]
# print("List before function call",List1)
# myFunc2(List1)
# print("List after function call",List1)
# List1 = [1]
# print("List before function call",List1)
# myFunc3(List1)
# print("List after function call",List1)
# a = int(input("Enter the value of temperature:"))
# print(tempConversion.centigrade(a))
# print(tempConversion.fahrenheit(a))
# print(abs(2))
# print(divmod(12,2))
# print(sum([2,4,5]))
# print(min([2,4,5]))
# print(max([2,4,5]))
# a = 24
# print(oct(a))
# print(hex(a))
# print(bin(a))
# a = 23.53353
# print(round(a))
num = float(input("Enter the value:"))
tnum = int(num)
rnum = round(num)
print("The conversion of 'num' with integer is:",tnum)
print("The conversion of 'num' with rounding is:",rnum)