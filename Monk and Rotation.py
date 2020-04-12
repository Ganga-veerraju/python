t=int(input())
for i in range((t)):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    y=x%n
    print(*(a[n-y:]+a[0:n-y]))
