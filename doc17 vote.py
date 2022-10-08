'''
 Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )
'''
def age(a):
          if a>=18:
                    print("eligible for vote")
          else:
                    print("your not eligible for vote")
age(int(input("enter your age:")))