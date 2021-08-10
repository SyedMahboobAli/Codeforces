t=int(input())
while(t):
    w=input()
    x=int(input())
    s=""
    a=0
    for i in range(1,len(w)+1):
        f=0
        if(i>x):
            if(w[i-x]=='1'):
                s+='1'
                f=1
            else:
                s+='0'
        else::
            if(i+x==len(w)):
                s+='0'
                continue
            else:
                y=i+x
            if(w[y]=='1'):
                s+='1'
                f=1
            else:
                s+='0'
        else:
            a=1
            break
        
            
    if(a==1):
        print(-1)
        continue
    if(len(s)==0):
        print(-1)
    else:
        print(s)
    t-=1
