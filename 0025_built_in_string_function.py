# ********<str>.join()********
# print("*".join("Sankalp"))
# print("**".join("Sharma"))
# print("$$".join(["Sankalp","Sharma"]))
# print("$$".join(["Mr.","Sankalp","Sharma",]))

# ********<str>.split()********
# print("Sankalp Sharma is a python programmer.".split())
# print("Sankalp Sharma is a python programmer.".split("a"))

# ********<str>.replace()********
# print("Sankalp Sharma is a python programmer.".replace("python","cpp"))

# Encryption of string
def encryption(enkey, strr):
    return enkey.join(strr)
def decryption(enkey, strr):
    return strr.split(enkey)

strr = input("Enter the string you want to encrypt:")
enkey = input("Enter the encryption key you want in your string:")
print("The encrypted string is:",encryption(enkey, strr))
print("The decrypted string is:",decryption(enkey, strr))
