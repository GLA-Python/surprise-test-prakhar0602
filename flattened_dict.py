a=eval(input())
y=True
def flatdict(d):
    e={}
    for i in d:
        if str(type(d[i]))=="<class 'dict'>":
            for j in d[i]:
                e[str(i)+"."+str(j)]=d[i][j]
        else:
            e[i]=d[i]
    return e
while y:
    z=0
    for i in a:
        if str(type(a[i])) == "<class 'dict'>":
            z+=1
    if z!=0:
        a=flatdict(a)
    else:
        y=False
print(a)