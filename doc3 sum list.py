'''Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Output : 20.
'''
def sum_list(a):
          sum=0
          for i in a:
                    sum=sum+i
          return sum
print(sum_list([8,2,3,0,7]))
