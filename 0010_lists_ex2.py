list1 = ["a","b","c"]
list2 = ["h","i","t"]
list3 = [1,2,3]
print(list1)
print(list2)
print(list3)

list3.extend(list1)
list3.extend(list2)

print(list3)