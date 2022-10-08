'''Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of consecutive numbers with any constant difference between numbers. Print False otherwise. 
Sample Input:
2 4 6 8
Sample Output:
True
Sample Input:
-5 -6 -7 -8
Sample Output:
True
Sample Input:
'''
def consecutive(a):
    i=0
    k=a[1]-a[0]
    while i<len(a)-1:
        v=a[i+1]-a[i]
        if v!=k:
            return False
        i=i+1
    return True
print(consecutive([4,5,6,7,8,9,10]))
print(consecutive([45,46,47,49,50,53]))

