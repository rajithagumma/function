'''Kids drink toddy.
	Teens drink coke.
	Young adults drink beer.
	Adults drink whisky.
	Make a function that receive age, and return what they drink.
Rules:-
Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
'''
def drink(a):
    if a<14:
        return "Kids drink toddy"
    elif a<18:
        return "Teens drink coke"
    elif a<21:
        return "Young adults drink beer"
    elif a>21:
        return "Adults drink whisky"
print(drink(int(input("enter the age:"))))
