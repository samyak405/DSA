arr=[]
total = int(input("enter total number of elements:"))
print("enter elemenets:")
for i in range(total):
    num = int(input())
    arr.append(num)
print ("the numbers are:", arr)

count_even=0
count_odd=0
for i in arr:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even numbers:", count_even)
print("Odd numbers:", count_odd)