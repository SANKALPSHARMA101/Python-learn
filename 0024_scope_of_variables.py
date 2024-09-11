# Global Variable
x = 5 
def func(a):
    b = a + 1
    return b
y = int(input("Enter the number"))
z = y + func(x)
print(z)

def calcSum(a,b,c):
    return a+b+c

def average(x,y,z):
    sm = calcSum(x,y,z)
    return sm/3

num1 = int(input("Enter the value of first integer:"))
num2 = int(input("Enter the value of second integer:"))
num3 = int(input("Enter the value of third integer:"))
print("Average of the provided3 numbers is:",average(num1, num2, num3))