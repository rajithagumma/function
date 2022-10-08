def fun(n):
    if n==0:
        return 0
    else:
        return fun(n-1)+n**2
n=int(input("enter the number:"))
result=fun(n)
print(result)
