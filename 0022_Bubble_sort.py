aList  = [15,6,13,22,3,52,2]
print("The original list is:",aList)
n = len(aList)

for i in range(n):
    for j in range(n-i-1):
        if aList[j] > aList[j+1]:
            aList[j],aList[j+1] = aList[j+1],aList[j]
print("List after sorting the elements:",aList)