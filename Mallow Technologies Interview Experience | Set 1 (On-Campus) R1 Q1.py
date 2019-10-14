t=int(input())
a=list(map(int,input().split()))
s=0
a=sorted(a)
for i in range(0,len(a)-2):
    for j in range(1,len(a)-1):
        for k in range(2,len(a)):
            
            if(i!=j and j!=k and k!=i and a[i]+a[j]+a[k]<=t):
                if(a[i]<a[j]<a[k]):
                    s+=1
print(s)
