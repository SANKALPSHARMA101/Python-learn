T = ("s","a","n","k","a","l","p")
char = (input("Enter the character you want to find in tuple T:"))
if char in T:
    count = 0
    for a in T:
        if a!=char:
            count += 1
        else:
            break
    print(char,"is present in tuple T.")
else:
    print(char,"is not present in tuple T.")