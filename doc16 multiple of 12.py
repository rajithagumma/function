'''Print multiplication table of 12 using function.'''
def table(a):
          i=1
          while i<=10:
                    print(a,"x",i,"=",a*i)
                    i=i+1
table(int(input("enter the number:")))