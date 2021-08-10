t=int(input())
while(t):
    n,m=map(int,input().split())
    a=[]
    
    for i in range(n):
        x=list(input())
        a.append(x)
    for i in range(n):
        count1=0
        count0=0
        for j in range(m):
            if(a[i][j]=='0'):
                count0+=1
            elif(a[i][j]=='1'):
                count1+=1
        print(count0,count1)
        
    t-=1
