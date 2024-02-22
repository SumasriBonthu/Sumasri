n,m=map(int,input().split(" "))
if m>n:
    print(0)
else:
    c=n-m
    if c%4==0:
        np=c//4
    else:
        np=(c//4)+1
print(np)
