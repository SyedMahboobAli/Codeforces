t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=set(l)
    l=list(l)
    l.sort()
    l.append(0)
    f=0
    for i in range(len(l)):
        if(i==len(l)-1):
            break
        if(l[i+1]-l[i]>1):
            f=1
            break
    if(f==0):
        print("YES")
    else:
        print("NO")
    
    t-=1
