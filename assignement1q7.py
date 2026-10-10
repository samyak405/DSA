arr = []

total = int(input("Enter total number of elements: "))

print("Enter elements:")

for i in range(total):
    num = int(input())
    arr.append(num)

print("The numbers are:", arr)

# Print non-zero elements first
for i in range(total):
    if arr[i] != 0:
        print(arr[i], end=" ")

# Print zeros at the end
for i in range(total):
    if arr[i] == 0:
        print(arr[i], end=" ")

print()