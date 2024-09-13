import sys
new_one = open("c:\\SAMPLE\\new_one\\Answer.txt", "w")
# line1 = new_one.readline()
# line2 = new_one.readline()
# sys.stdout.write(line1)
# sys.stdout.write(line2)
# sys.stderr.write("No error occurred\n")
with open("c:\\SAMPLE\\new_one\\Answer.txt","w") as new_one:
    new_one.write("Hi there!!")
new_one.close()