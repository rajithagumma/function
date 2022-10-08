'''raw a flowchart to take a list of N numbers from the user, print True if the complete list consists of consecutive numbers with a difference of one. Print False otherwise. 

Sample Input:
1 2 3 4 5 6 7
Sample Output:
True
Sample Input:
45 46 47 48 49 51 52
Sample Output:
False
Sample Input:
4 5 6 7 8 9 10
'''
def consecutive(a):
    i=0
    while i<len(a)-1:
        v=a[i+1]-a[i]
        if v!=1:
            return False
        i=i+1
    return True
print(consecutive([4,5,6,7,8,9,10]))
print(consecutive([45,46,47,49,50,53]))

