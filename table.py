user=int(input("enter the number:"))
i=1
while i<=10:
    j=1
    while j<=user:
        print(j,"*",i,"=",i*j,end="  ")
        j=j+1
    i=i+1
    print()