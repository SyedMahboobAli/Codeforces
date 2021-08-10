n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m1=min(b)
m2=max(b)
m3=[]
for i in range(len(a)):
    if(a[i]<=m1):
        c=a[i]&m2
        m3.append(c)
    else:
        c=a[i]&m1
        m3.append(c)
x=m3[0]
for i in range(1,len(m3)):
    x|=m3[i]
print(x)
