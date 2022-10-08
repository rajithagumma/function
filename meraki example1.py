# n=int(input("enter the number of rows:"))
# i=1
# while i<=n:
#           j=1
#           while j<=i:
#                     print(i,end=" ")
#                     j=j+1
#           k=i
#           while k<=4:
#                     print(k+1,end=" ")
#                     k=k+1
#           i=i+1
#           print()


i=0
v=ord("U")
while i<5:
          j=0
          while j<5:
                    print(chr(v),end=" ")
                    j=j+1
                    v=v+1
          i=i+1
          v=v-10
          print()