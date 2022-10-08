'''I would like to be able to pass an array with two elements 
to my swapValues function to swap the values. However it appears 
that the values aren't changing.
Can you figure out what's wrong here?

'''
def swap(a):
          b=[]
          a[0],a[1]=a[1],a[0]
          b.append(a[0])
          b.append(a[1])
          return b
print(swap([12,14]))

