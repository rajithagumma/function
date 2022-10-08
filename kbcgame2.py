name=input("enter your name:")
question=["1.how many schedules are there indian constitution","2.father of local governments in india",
"3.who is the first women president indian national congress","4.where is the international rice research centre"]
option=[["a.Eight","b.ten","c.twelve","d.nine"],["a.Lorddafrin","b.Lord litton","c.waren hasting","d.Lord rippon"],
["a.Annie Bessant","b.Sarojini naidu","c.Indira gandhi","d.prathiba patel"],
["a.kotak","b.Manila","c.The Hague ","d.India"]]
solu=["c","d","a","b"]
life_line=[["a.Eight","b.twelve"],["a.warenhasting","b.lord rippon"],["a.annie besant","b.Indhira gandhi"],
["a.manila","b.india"]]
life_solution=["b","b","a","a"]
price=[" WONNERFUL ANSWER!YOU WON 10000 RUPEES","CONGRASLATIONS you won 15,000","WOW!GREAT ANSWER you won 25,000","AWESOME,YOU ARE WINNER KBC GAME you won 100000 rupees"]
i=0
count=0
def fifty(i):
    global count
    if count==0:
        count+=1
        k=0
        while k<len(life_line[i]):
            print(life_line[i][k])
            k=k+1
        choice=input("enter your answer")
        if choice==life_solution[i]:
            return True
        else:
            return False
                
    else:
        print("already used lifeline")
        choice=input("enter your answer....")
        if choice==solu[i]:
            return True
        else:
            return False
def solution(i):
    print("5050")
    choice=input("enter your answer...")
    if choice=="5050":
        return fifty(i)
    else:
        option[i]
        if choice==solu[i]:
            return True
        else:
            return False
def ques():
    i=0
    while i<len(question):
        print(question[i])
        j=0
        while j<len(option[i]):
            print(option[i][j])
            j=j+1
        a=solution(i)
        if a==False:
            print("wrong answer")
            break
        elif a==True:
            print("congrats",price[i])
            
        i=i+1
ques()