'''Given the same list, print the last 
‘N’ elements in reverse order.
Sample Input:
2
Sample Output:
q
b 
Sample Input:
3
Sample Output:
q
b 
5

'''
def last(a):
          n=int(input("enter the number"))
          i=-1
          while i>=-n:
                    print(a[i])
                    i=i-1
last(["a",1,2,5,"b","q"])