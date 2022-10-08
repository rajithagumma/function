'''
Q4.Write a Python program to reverse a string.
Sample String : "1234abcd"
Output : "dcba4321".
'''
def reverse(a):
          i=-1
          b=""
          while i>=-len(a):
                    b=b+a[i]
                    i=i-1
          return b
print(reverse("1234abcd"))
