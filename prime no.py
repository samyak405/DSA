num = int(input("Enter a number: "))
for i in range(2,(num//2)+1):
    if num % i == 0:
        flag = 0
        break
if flag == 0:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")