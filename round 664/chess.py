n,m,sx,sy=map(int,input().split())
print(sx,sy)
for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==sx and j==sy):
            continue
        else:
            print(i,j)
