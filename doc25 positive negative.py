'''
 Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
Example:
list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

'''
def numbers(list):
          positive=0
          negative=0
          for i in list:
                    if i>0:
                              positive+=1
                    else:
                              negative+=1
          print("positive =",positive,",","negative =",negative)
numbers([2, -7, 5, -64, -14])