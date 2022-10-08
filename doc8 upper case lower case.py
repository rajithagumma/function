'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Uppercase characters : 3
No. of Lower case Characters : 12

'''
def case(a):
    upper=0
    lower=0
    for i in a:
        if i.isupper()==True:
            upper=upper+1
        elif i.islower()==True:
            lower+=1
    print("no.of upper case characters",upper)
    print("no.of lower case characters",lower)
v=input("enter the string:")
case(v)

        

