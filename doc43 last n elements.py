'''Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. 
Print the last ‘N’ elements of the given list. ‘N’ is accepted 
from the user.
Sample Input:
1
Sample Output:
q 
Sample Input:
3
Sample Output:
5
b 
q
'''
def last(a):
          n=int(input("enter the number"))
          i=-n
          while i<=-1:
                    print(a[i])
                    i=i+1
last(["a",1,2,5,"b","q"])