'''Your task is to make two functions, max and min (maximum and minimum in 
PHP and Python, maxi and mini in Julia) that take a(n) array/vector
 of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.
#Examples:-

maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5.

minimun([42, 54, 65, 87, 0]) returns 0.
'''

def maximum(a):
          max=-1000000
          for i in a:
                    if i>=max:
                              max=i
          return max

print(maximum([4,6,2,1,9,63,-134,566]))
print(maximum([5]))
def minimum(a):
          min=1000000
          for i in a:
                    if i<=min:
                              min=i
          return min
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(minimum([42, 54, 65, 87, 0]))

