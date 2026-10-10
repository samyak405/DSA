arr=[]
total = int(input("enter total number of elements:"))
print("enter elemenets:")
for i in range(total):
    num = int(input())
    arr.append(num)
print ("the numbers are:", arr)
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print ("the new numbers are:", new_arr)