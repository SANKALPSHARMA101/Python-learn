import os
os.chdir('c:\\Users')
# print(os.getcwd())
# print(os.listdir())
os.chdir('c:\\SAMPLE')
# print(os.mkdir("Test"))
# print(os.mkdir("lol.py"))
# os.rename('Test','new_one')
# new_one= open("c:\\SAMPLE\\new_one\\lol.txt","r")
# new_one= open("c:\\SAMPLE\\new_one\\abc.txt","w")
# new_one= open("c:\\SAMPLE\\new_one\\abc.txt","a",)
# with open("c:\\SAMPLE\\new_one\\lol.txt","a") as new_one:
#     new_one.write("Hello guys!!!")
# new_one.close()
# new_one = open("cricket_academy_in_delhi.txt","w") -->>!!!!!!!!!!
# print(new_one.readline(20))
# print(new_one.readlines())
# str = new_one.read(12)
# print(str)
# str2 = new_one.read(25)
# print(str2)
# str = new_one.read(12)
# print(str, end = ' ')
# str2 = new_one.read(25)
# print(str2, end = '  ')
# str = ' '
# while str:
#     str = new_one.readline()
#     print(str, end = ' ')
# str = new_one.readline()
# file_size = len(str)
# print("The length of the file is:",file_size)
# print("Number of lines in the given text file is:",len(new_one.readlines()))
# new_one.write("Enjoy the blog guys!!\n")     #--> This function helps in writing new content by completely erasing the previous content in the file.
# new_one.write("Guys this is the famous blog regarding the famous cricketers and their cricket academies" 
#               " from their hometown or birth place which is Delhi.\nThis"
#               " blog is going to be a great knowlegable and informative"
#               " one I hope you all will enjoy it.")     #--> This function helps in writing without removing the previous written content in the file.
# new_one = open("C:\\SAMPLE\\new_one\\lol.txt","w") -->>!!!!!!!!!
# ********Writing name of students by using write function********
# for i in range(4):
#     name = input("Enter the name of the student:")
#     new_one.write(name)
#     new_one.write('\n')

# ********Writing name of students without using write function********
# list1 = []
# for i in range(4):
#     name = input("Enter the name of the students:")
#     list1.append(name + '\n')
#     new_one.writelines(list1)
    
# new_one = open("c:\\SAMPLE\\new_one\\Marks.txt","w")
# count = int(input("Enter the no of students in the class:"))
# for i in range(count):
#     print("Enter the details for the students",(i+1),"below:")
#     rollno = int(input("Roll no:"))
#     name = input("Name:")
#     marks = float(input("Marks:"))
#     rec = str(rollno) +","+ name +","+ str(marks)+'\n'
#     new_one.write(rec) 
    
# new_one = open("c:\\SAMPLE\\new_one\\Marks.txt","r") -->>!!!!!!!!
# for i in range(2):
#     print("Enter the details for the students",(i+1),"below:")
#     rollno = int(input("Roll no:"))
#     name = input("Name:")
#     marks = float(input("Marks:"))
#     rec = str(rollno) +","+ name +","+ str(marks)+'\n'
#     new_one.write(rec) 

# print(new_one.readlines())
new_one = open("c:\\SAMPLE\\new_one\\Answer.txt","r")
# line = " "
# while line:
#     line = new_one.readline()
#     for word in line.split():
#         print(word, end = '#')
#     print()

ch = " "
vcount = 0
ccount = 0
while ch:
    ch = new_one.read(1)
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        vcount = vcount + 1
    else:
        ccount = ccount + 1
print("Vowels in the context in the file is:",vcount)
print("Consonants in the context in the file is:",ccount)
new_one.rstrip('\n')

new_one.close()
