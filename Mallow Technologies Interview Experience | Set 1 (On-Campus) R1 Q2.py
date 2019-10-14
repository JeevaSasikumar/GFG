def gcd(s):
    x=0
    if(s==1):
        if(x%2==0):
            return "Richard"
        else:
            return "Lousie"
    if(s in c):
        x+=1
        s=s//2
        return gcd(s)
    else:
        for i in range(1,100):
            if(c[i]>s):
                x+=1
                s=s-c[i-1]
                return gcd(s)
                
        
a=int(input())
c=[]
for i in range(1,100):
    c.append(2**i)
while(a>0):
    a=a-1
    b=int(input())
    d=gcd(b)
    print(d)
