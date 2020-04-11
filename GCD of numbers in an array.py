def gcd(a,b):
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd        
l=list(map(int,input("enter the numbers:").split()))
n1=l[0]
n2=l[1]
g=gcd(n1,n2)
for i in range(2,len(l)):
    g=gcd(g,l[i])
print("gcd is:",g)
