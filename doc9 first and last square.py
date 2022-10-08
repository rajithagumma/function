'''Write a Python program to generate and print a list of first and last 5 elements where 
  the values are square of numbers between 1 and 30 (both included).
Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).'''

def square():
    i=1
    j=30
    c=[]
    d=[]
    while i<=30:
        if i<=5:
            c.append(i*i)
        elif i>=25:
            d.append(i*i)
        i=i+1
    e=c,d
    print(e)
square()





