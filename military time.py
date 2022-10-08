print("please give time like this 07:12:23AM(hh:mm:sec AM or PM)")
a=input("enter the time:")
if a[-2:]=="AM" or a[-2:]=="am":
    if a[:2]=="12":
        print("00"+a[2:-2])
    else:
        print(a[:-2])
else:
    hour=int(a[:2])
    if hour<12:
        hour=hour+12
        print(str(hour)+a[2:-2])

# def timeconversion(a):
#     if a[-2:]=="AM":
#         if a[:2]=="12":
#             return "00"+a[2:-2]
#         else:
#             return a[:-2]
#     else:
#         hour=int(a[:2])
#         if hour<12:
#             hour=hour+12
#             return str(hour)+a[2:-2]
# print("give time like this 07:12:23AM(hh:mm:sec AM or PM)")
# time=input("enter the time:")
# print(timeconversion(time))


