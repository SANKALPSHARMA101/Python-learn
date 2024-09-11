info = {"Sankalp":"Maths","Keshav":"Science","Mahak":"Music","Divyansh":"Gaming"}
ask = input("Enter the value of whose key you want to search:")
if ask in info.values():
    for a in info:
        if info[a] == ask:
            print("The key for the",ask,"value is",a)
            break
else:
    print("There is no such existing value in the dictonary")