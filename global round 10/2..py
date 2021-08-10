for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    i=n-1
    s=0
    while(k):
        s+=l[i]
        i-=1
        k-=1
        
    for i in range(len(l)):
        print(l[i]-s,end=' ')
    print()
    
    
