t=int(input())
while(t):
    n,m=map(int,input().split())
    a=[]
    count=0
    for i in range(n):
        x=list(input())
        a.append(x)
    for i in range(n):
        if(a[i][m-1]=='R'):
            count+=1
    for i in range(m):
        if(a[n-1][i]=='D'):
            count+=1
    print(count)
        
    t-=1
