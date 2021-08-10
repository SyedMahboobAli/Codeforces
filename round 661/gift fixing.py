t=int(input())
while(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a1=min(a)
    b1=min(b)
    move=0
    for i in range(n):
        if(a[i]>a1 and b[i]>b1):
            x=min(a[i]-a1,b[i]-b1)
            a[i]-=x
            b[i]-=x
            move+=x
        if(a[i]>a1):
            move+=a[i]-a1
        if(b[i]>b1):
            move+=b[i]-b1
    
    print(move)        
    t-=1
