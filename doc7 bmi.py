'''Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

'''
def body(weight,height):
          height2=height/100
          bmi=weight/height2**2
          if bmi<=18.5:
                    return "underweight"
          elif bmi<=25.0:
                    return "normal"
          elif bmi<=30.0:
                    return "overweight"
          elif bmi>30:
                    return "obese"
                    
a=int(input("enter your weight:"))
b=int(input("enter your height in cm:"))
print(body(a,b))
