line = input("Enter a line: ")
lowercount = uppercount = 0
digitcount = alphacount = 0
for a in line:
    if a.islower():
        lowercount += 1
    if a.isupper():
        uppercount += 1
    if a.isalpha():
        alphacount += 1
    if a.isdigit():
        digitcount += 1

print("No. of lower-character in the given line is:" , lowercount)
print("No. of upper-character in the given line is:" , uppercount)
print("No. of alpha-character in the given line is:" , alphacount)
print("No. of digits in the given line is:" , digitcount)


