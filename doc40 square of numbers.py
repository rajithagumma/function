'''Write a function For example, if we give 9119  the function 
should return  811181, as the  square of 9 is 81 and square of 1  is 1.
'''
def square(l):
    b=[]
    i=0
    while i<len(l):
        n=l[i]
        while n>0:
            r=n%10
            t=r*r
            n=n//10
            print(t,end="")
        i=i+1
square([9119])

