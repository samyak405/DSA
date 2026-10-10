arr=[]
total = int(input("enter total number of elements:"))
print("enter elements:")
for i in range(total):
    num = int(input())
    arr.append(num)
print ("the numbers are:", arr)

print("the array in reverse order is:")
for i in range(total-1,-1,-1):
    print(arr[i], end=" ")

