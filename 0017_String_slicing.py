# import string
name = "sankalp is a student"

print(name[2:5])
print(name[-5:-2])
print(len(name))
print(name.capitalize())    # First letter of the string gets capitalized
print(name.upper())     # All letters in string get capitalized
print(name.lower())     # All letters in string get lower-case
print(name.title())     
print(name.isalnum())     # All letters in string should be only alphabet or number nothing else(no space bar also).
print(name.isalpha())     # All letters in string should be only alphabets
print(name.isdigit())     # All letters in string should be only digits
print(name.isspace())     # All letters in string should be only space
print(name.islower())     # All letters in string should be only in lower-case
print(name.isupper())     # All letters in string should be only in upper-case
print(name.istitle())     # All first letters in string should be only in upper-case

a = "Mango Is a fRiut."
print(a.startswith("M"))
print(a.endswith("ut."))
print(a.swapcase())
print(a.partition("a"))
print(a.count("a"))
print(a.lstrip("Man"))
print(a.rstrip("iut."))
