'''.Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5].'''

def unique(a):
          c=[]
          for i in a:
                    if i not in c:
                              c.append(i)
          return c
print(unique([1,2,3,3,3,4,5]))