import sys
import pickle
# new_one = open("c:\\SAMPLE\\new_one\\Answer.txt", "w")
# line1 = new_one.readline()
# line2 = new_one.readline()
# sys.stdout.write(line1)
# sys.stdout.write(line2)
# sys.stderr.write("No error occurred\n")
# with open("c:\\SAMPLE\\new_one\\Answer.txt","w") as new_one:
#     new_one.write("Hi there!!")
# new_one.close()
# emp1 = {"Empno":1201,"Name":"Anushree","Age":25,"Salary":47000}
# emp2 = {"Empno":1211,"Name":"Zoya","Age":30,"Salary":48000}
# emp3 = {"Empno":1251,"Name":"Simarjeet","Age":27,"Salary":49000}
# emp4 = {"Empno":1266,"Name":"Alex","Age":29,"Salary":50000}
# emp_file = open("c:\\SAMPLE\\new_one\\emp.dat","wb")
# pickle.dump(emp1, emp_file)
# pickle.dump(emp2, emp_file)
# pickle.dump(emp3, emp_file)
# pickle.dump(emp4, emp_file)
# emp_file.close()

stu = {}
stu_file = open("c:\\SAMPLE\\new_one\\Student.dat","wb")
ans = "y"
while ans == "y":
    roll_no = int(input("Enter the roll no of the student:"))
    name = input("Enter the name of the student:")
    marks = float(input("Enter the marks of the student:"))
    stu["Rollno"] = roll_no
    stu["Name"] = name
    stu["Marks"] = marks
    pickle.dump(stu, stu_file)
    ans = input("Do you want to enter more records? (y/n)")
stu_file.close()