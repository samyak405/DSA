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

