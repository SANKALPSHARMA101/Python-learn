n = (int(input("Enter no of students??")))
Comp = {}
for a in range(n):
    key = input("Enter the name of student:")
    value = int(input("Enter no of competition won:"))
    Comp[key] = value
print("The dictonary for the students and their competition won:", Comp)
