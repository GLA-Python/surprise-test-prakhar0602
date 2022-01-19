n=int(input())
a="1"
for i in range(n):
    c=1
    b=""
    if i==0:
        print(a)
    else:
        a+=" "
        for j in range(1,len(a)):
            if a[j]==a[j-1]:
                c+=1
            else:
                b+=str(c)+a[j-1]
                c=1
        print(b)
        a=b