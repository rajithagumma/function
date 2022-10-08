a=["narani","priyanka"]
b=["web","json"]
k="isdoing"
i=0
d=[]
n=[]
while i<len(a)-1:
          l=a[i]+k+b[i]
          m=a[i+1]+k+b[i+1]
          d.append(l)
          n.append(m)
          i=i+1
print(d)
print(n)