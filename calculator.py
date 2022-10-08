def add(a,b):
          return a+b
def sub(a,b):
          return a-b
def mul(a,b):
          return a*b
def divide(a,b):
          return a/b
def main(a,b,operator):
          if operator=="+":
                    print(add(a,b))
          elif operator=="-":
                    print(sub(a,b))
          elif operator=="*":
                    print(mul(a,b))
          elif operator=="/":
                    print(divide(a,b))
v=int(input("enter the number :"))
r=int(input("enter the number:"))
operation=input("enter the operator:")
main(v,r,operation)
