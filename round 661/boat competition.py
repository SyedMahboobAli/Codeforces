try:
    # TODO: write code...
    t=int(input())
    while(t):
        n=int(input())
        a=list(map(int,input().split()))
        l=[]
        for i in range(n):
            for j in range(i+1,n):
                s=a[i]+a[j]
                l.append(s)
        s=set(l)
        m=[]
        for i in s:
            x=l.count(i)
            abc=[i,x]
            tupl=tuple(abc)
            m.append(tupl)
        m.sort(key=lambda x:x[1])
        count=0
        sum1=m[-1][0]
        for i in range(n):
            for j in range(i+1,n):
                sum2=a[i]+a[j]
                if(sum1==sum2):
                    count+=1
                    a[i]=0
                    a[j]=0
        print(count)
        t-=1
except:
    pass
