n=int(input())
for i in range(n):
    a,b,k=map(int,input().split())
    if a<=b:
        print(k//a)
    else:
        print(k//b)