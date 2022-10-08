'''Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
 ist=['abc', 'xyz', 'aba', '1221']
result= 2.

'''
def word(a):
    count=0
    for i in a:
        if len(i)>1 and i[0]==i[-1]:
            count+=1
    return count
print(word(['abc', 'xyz', 'aba', '1221']))

def word(a):
    i=0
    count=0
    while i<len(a):
        if len(a[i])>1 and a[i][0]==a[i][-1]:
            count+=1
        i=i+1
    return count
print(word(['abc', 'xyz', 'aba', '1221']))


