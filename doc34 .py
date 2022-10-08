def list(a):
          i=0
          max=0
          second_max=0
          while i<len(a):
                    if a[i]>=max:
                              max=a[i]
                    elif a[i]>=second_max and a[i]!=max:
                              second_max=a[i]
                    i=i+1
          # print(max)
          # print(second_max)
          return max+second_max
print(list([10,14,2,23,19]))
print(list([99,2,2,23,19]) )    
                    
