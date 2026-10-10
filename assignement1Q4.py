arr = []

total = int(input("Enter total number of elements: "))

print("Enter elements:")
for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are:", arr)

search = int(input("Enter element to be searched: "))

found = False

for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index:", i+1)
        found = True
        break

if found == False:
    print("Element not found")