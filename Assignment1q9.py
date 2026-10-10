s = input("enter a string:").lower()
v=c=d=sp=0
for i in s:
    if i in "aeiou":
        v+=1
    elif i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1
    else:
        sp+=1
print("vowels:",v)
print("consonants:",c)
print("digits:",d)
print("symbols:",sp)