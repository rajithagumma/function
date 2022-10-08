'''Write a function that prints all the prime numbers between 0 
and limit where limit is a parameter.
'''
def prime(a):
    i=0
    while i<a:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c=c+1
            j=j+1
        if c==2:
            print(i)
        i=i+1
prime(int(input("enter the  limit:")))