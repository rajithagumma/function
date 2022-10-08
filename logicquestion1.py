# a=int(input("enter the number:"))
# while a>=10:
#           sum=0
#           while a>0:
#                     r=a%10
#                     sum=sum+r

# l=[1,0,2,0,3,0,4,5,0,6,0,7,9,8,0,8]
# i=0
# b=[]
# c=[]
# while i<len(l):
#           if l[i]==0:
#                     b.append(l[i])
#           else:
#                     c.append(l[i])
#           i=i+1
# b.extend(c)
# print(b)
    
# a=["archana","rajitha",1,2,3.5,4.5]
# i=0
# b=[]
# c=[]
# d=[]
# while i<len(a):
#           if type(a[i])==str:
#                     b.append(a[i])
#           elif type(a[i])==int:
#                     c.append(a[i])
#           else:
#                     d.append(a[i])
#           i=i+1
# print(b)
# print(c)
# print(d)


# a=[3,5,2,1,6,9]
# i=0
# b=[]
# while i<=len(a)-1:
#           k=str(a[i])+str(a[i+1])
#           b.append(int(k))
#           i=i+2
# print(b)

# a=[1,3,2,1]
# b=a[0]
# i=1
# c=[]
# while i<len(a):
#           k=a[i]-b
#           c.append(k)
#           i=i+1
# print(c)


a=[10,20,[30,40,[50,60],70],80,90]
a[2][2].insert(2,7000)
print(a)