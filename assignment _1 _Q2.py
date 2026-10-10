#q1
arr=[]
total = int(input("enter total number of elements:"))
print("enter elemenets:")
for i in range(total):
    num = int(input())
    arr.append(num)
print ("the numbers are:", arr)
sum = 0
for i in range(arr.__len__()):
    sum += arr[i]

print("the sum is", sum)

max_num = max(arr)
print("the max is", max_num)
min_num = min(arr)
print("the min is", min_num)
for i in range(arr):
    if i>max_num:
        max_num = i
    if i<min_num:
        min_num = i

 print("the max is", max_num)
 print("the min is", min_num)