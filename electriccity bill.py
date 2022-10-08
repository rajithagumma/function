units=int(input("enter the n.of units:"))
if units<=100:
          print("no charge")
elif units<=200:
          print((units-100)*5)
elif units>200:
          print((100*5)+(units-200)*10)

days=int(input("enter the number f days:"))
if days<=5:
          print(days*2)
elif days>=6 and days<=10:
          print((5*2)+(days-5)*3)
elif days>10 and days<=15:
          print((5*2)+(5*3)+(days-10)*4)
elif days>15:
          print((5*2)+(5*3)+(5*4)+(days-15)*5)