t=int(input())
for _ in range(t):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	p=min(a)
	c=k-p
	if(c<0):
		print("0")
	else:
		print(c)

