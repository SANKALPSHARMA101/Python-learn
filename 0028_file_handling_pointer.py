import sys
new_one = open("c:\\SAMPLE\\new_one\\Answer.txt")
line1 = new_one.readline()
line2 = new_one.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write("No error occurred\n")
new_one.close()