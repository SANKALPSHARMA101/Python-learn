ok = False
while not ok:
    try:
        numberstring = input("Enter an integer:")
        n = int(numberstring)
        ok = True
    except:
        print("Error!!Not a valid integer.")