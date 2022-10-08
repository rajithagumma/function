def a(n,option,solution):
    i=0
    while i<len(n):
        print(n[i])
        j=0
        while j<len(option):
            print(option[j])
            j=j+1
        choose=int(input("enter your choice"))
        if choose==solution[i]:
            print("congrates")
        else:
            print("wrong answer")
            print("try again")
        i=i+1
n=[" who is the founder of facebook"]
option=["1.mark zuckerberg","2.bill gates","3.steve jobs","4.larry page"]
solution=[1]
a(n,option,solution)