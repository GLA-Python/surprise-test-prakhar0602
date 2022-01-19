def expanding(I):
    c=0
    y=0
    for i in range(1,len(I)):
        a=I[i-1]
        b=I[i]
        if a>b:
            x=a-b
        else:
            x=b-a
        if x<=y:
            c+=1
            break
        y=x
    if c==0:
        return True
    else:
        return False
a=eval(input())
print(expanding(a))