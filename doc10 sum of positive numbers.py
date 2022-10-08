'''reate a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

"4",  "5" --> "9"
"34", "5" --> "39"
Notes:

If either input is an empty string, consider it as zero.

'''
# def positive(a,b):
#           sum=int(a)+int(b)
#           a=str(sum)
#           print(repr(a))
# i=input("enter the number:")
# j=input("enter the number:")
# positive



a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
if a>b and a<c:
          if b>c:
                    print(b," is median")
          else:
                    print(c,"is median")
if b>c and b>a:
          if c>a:
                     print (c,"is median")
                      
          else:
                    (a,"is median")
if c>a and c>b:
          if a>b:
                    print()

 




