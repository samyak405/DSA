n=7
mid= n//2
for i in range(n):
    for j in range(n):
        if i==mid or j==mid:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()