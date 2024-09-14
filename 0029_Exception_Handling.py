# ok = False
# while not ok:
#     try:
#         numberstring = input("Enter an integer:")
#         n = int(numberstring)
#         ok = True
#     except:
#         print("Error!!Not a valid integer.")
# try:
#     new_one = open("c:\\SAMPLE\\new_one\\myfile.txt","w")
#     print(new_one.read())
# except:
#     print("Error opening file!!")
# finally:
#     print("Finally saying goodbye!!")
    
# try:
#     a = int(input("Enter the value of numerator:"))
#     b = int(input("Enter the value of denominator:"))
#     if b==0:
#         raise ZeroDivisionError(str(a) + "/0 not possible")
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Exception",str(e))

try:
    new_one = open("c:\\SAMPLE\\new_one\\myfile.txt")
    my_line = new_one.readline()
    my_int = int(new_one.strip())
    my_calc_value = 101/my_int
except IOError:
    print("I/O error occurred")
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Division by zero error occurred")
except:
    print("Unexcepted error")
else:
    print("Let's go!! No exceptions>")
    