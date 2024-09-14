import sys
import pickle
import csv
# new_one = open("c:\\SAMPLE\\new_one\\Answer.txt", "w")
# new_one = open("c:\\SAMPLE\\new_one\\myfile.txt", "wb")
# line1 = new_one.readline()
# line2 = new_one.readline()
# sys.stdout.write(line1)
# sys.stdout.write(line2)
# sys.stderr.write("No error occurred\n")
# with open("c:\\SAMPLE\\new_one\\Answer.txt","w") as new_one:
#     new_one.write("Hi there!!")
# emp1 = {"Empno":1201,"Name":"Anushree","Age":25,"Salary":47000}
# emp2 = {"Empno":1211,"Name":"Zoya","Age":30,"Salary":48000}
# emp3 = {"Empno":1251,"Name":"Simarjeet","Age":27,"Salary":49000}
# emp4 = {"Empno":1266,"Name":"Alex","Age":29,"Salary":50000}
# pickle.dump(emp1, emp_file)
# pickle.dump(emp2, emp_file)
# pickle.dump(emp3, emp_file)
# pickle.dump(emp4, emp_file)

# stu = {}
# stu_file = open("c:\\SAMPLE\\new_one\\Student.dat","wb")
# ans = "y"
# while ans == "y":
#     roll_no = int(input("Enter the roll no of the student:"))
#     name = input("Enter the name of the student:")
#     marks = float(input("Enter the marks of the student:"))
#     stu["Rollno"] = roll_no
#     stu["Name"] = name
#     stu["Marks"] = marks
#     pickle.dump(stu, stu_file)
#     ans = input("Do you want to enter more records? (y/n)")
# stu_file.close()
# emp = {}
# emp_file = open("c:\\SAMPLE\\new_one\\emp.dat","rb")
# try:
#     while True:
#         emp = pickle.load(emp_file)
#         print(emp)
# except EOFError:
#     emp_file.close()
# print("Initially file-pointer's position is at:", new_one.tell())
# print("Three bytes read are:",new_one.read(3))
# print("After previous read, current position of file pointer:",new_one.tell())
# new_one.seek(10)
# new_one.seek(10, 1)
# new_one.seek(10, 2)
# new_one.seek(10, 0)
# new_one.seek(-5, 1)
new_one = open("c:\\SAMPLE\\new_one\\myfile.csv", "w")
stuwriter = csv.writer(new_one)
stuwriter.writerow(['Rollno','Name','Marks'])
for i in range(3):
    print("Student record:",(i+1))
    rollno = int(input("Enter the roll no of student:"))
    name = input("Enter the name of the student:")
    marks = float(input("Enter the marks of the student:"))
    sturec = [rollno,name,marks]
    stuwriter.writerow(sturec)
new_one.close()