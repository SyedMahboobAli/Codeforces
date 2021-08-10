t=int(input())
while(t):
    r,g,b,w=map(int,input().split())
    if((r+g+b+w)==0):
        print("YES")
    elif(r==0 or w==0 or g==0 or b==0):
        print("NO")
    else:
        print("YES")
    
    t-=1
