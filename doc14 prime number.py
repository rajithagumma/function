'''Write a function to check if a number is prime or not.
'''
def prime(a):
          i=1
          count=0
          while i<=a:
                    if a%i==0:
                              count+=1
                    i=i+1
          if count==2:
                    return "prime numbr"
          else:
                    return "not prime number"
print(prime(int(input("enter the number"))))