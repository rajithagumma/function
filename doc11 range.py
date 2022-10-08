'''mplement a function named

generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
generate_range(1, 10, 3) # should return list of [1,4,7,10]
generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
Note
min < max
'''
def range(initial,ending,step):
          b=[]
          while initial<=ending:
                    b.append(initial)
                    initial+=step
          print(b)
range(2,10,2)
range(1,10,3)
