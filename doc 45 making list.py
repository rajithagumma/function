'''Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
If it is even, then multiply it by 100
If it is odd, then multiply it by -1 
Sample Input:
	23
	42 
	41 
	1
Sample Output:
	-23 
          4200
'''
def make():
          i=1
          b=[]
          while i<=10:
                    user=int(input("enter the number:"))
                    if user%2==0:
                              b.append(user*100)
                    else:
                              b.append(-user)
                    i=i+1
          return b
print(make())
