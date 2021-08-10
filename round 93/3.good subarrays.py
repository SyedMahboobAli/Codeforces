try:
    t=int(input())
    while(t):
        n=int(input())
        s=input()
        l3=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                s1=0
                len1=0
                for k in range(i,j):
                    s1+=ord(s[k])-48
                    len1+=1
                if(s1==len1):
                    l3+=1
        print(l3)
        t-=1
except:
    pass
