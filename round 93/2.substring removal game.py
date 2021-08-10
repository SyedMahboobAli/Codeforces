t=int(input())
while(t):
    l=list(input().split('0'))
    l1=[]
    for i in l:
        x=len(i)
        l1.append(x)
    l1.sort(reverse=True)
    a=0
    for i in range(len(l1)):
        if(i%2==0):
            a+=l1[i]
    print(a)
    t-=1
