t=int(input())
while(t):
    n=int(input())
    s=input()
    s1=""
    for i in range(n):
        x=s[i:i+n]
        s1+=x[i]
    print(s1)
    
    
    t-=1
