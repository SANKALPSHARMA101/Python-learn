# ok = False
# while not ok:
#     try:
#         numberstring = input("Enter an integer:")
#         n = int(numberstring)
#         ok = True
#     except:
#         print("Error!!Not a valid integer.")
try:
    new_one = open("c:\\SAMPLE\\new_one\\myfile.txt","w")
    print(new_one.read())
except:
    print("Error opening file!!")