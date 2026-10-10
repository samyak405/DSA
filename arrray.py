arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
min= arr[0]
max= arr[0]
s_min=arr[1]
s_max=arr[1]
for i in range(1,len(arr)):
    if arr[i] < min:
        s_min = min
        min = arr[i]
    if arr[i] > max:
        s_max = max
        max = arr[i]

print(min)
print(max)
print(s_min)
print(s_max)
