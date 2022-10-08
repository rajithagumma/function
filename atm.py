def check(a,m):
    if a==1:
        print("your available balance is",m)
        print("thanks for visiting state bank of india")
def withdrawal(a,m):
    if a==2:
        w=int(input("enter your withdrawal amount:"))
        if w<m:
            print("your amount withdrawal succesfull")
            print(m-w,"is your remaining amount")
            print("thanks for visiting state bank of india")
        else:
            print("enter valid amount")
def pin_generate(a):
    if a==3:
        print("OTP sent to your registered mobile number")
        OTP=input("enter your 6 digit otp:")
        if len(OTP)==6:
            otp=input("confirm your 6 digit  otp:")
            if OTP==otp:
                pin=int(input("enter your new pin"))
                print("your pin generation is successfull")
                print("thanks for visiting state bank of india")
            else:
                print("enter correct otp")
        else:
            print("enter 6 digit otp")
def quit(a):
    if a==4:
        print("quit")
        print("thanks for visiting state bank of india")
def main_fun():
    print("WELCOME TO STATEBANK OF INDIA")
    password=1234
    print("menu_")
    print("1_balance enquiry")
    print("2_withdrawal")
    print("3_pin generation")
    print("4_quit")  
    a=int(input("please choose your transactio"))
    m=28000



    
    if a==1:
        pin=int(input("enter your four digit pin:"))
        if pin==password:
            check(a,m)
            main_fun()
        else:
            print(" wrong pin enter the correct pin")
            main_fun()
    elif a==2:
        pin=int(input("enter your four digit pin:"))
        if pin==password:
            withdrawal(a,m)
            main_fun()
        else:
            print("wrong pin enter the correct pin")
            main_fun()
    elif a==3:
        pin=int(input("enter your four digit pin:"))
        if pin==password:
            pin_generate(a)
            main_fun()
        else:
            print("  wrong pin enter the correct pin")
            main_fun()
    elif a==4:
        pin=int(input("enter your four digit pin:"))
        if pin==password:
            quit(a)
            main_fun()
        else:
            print(" wrong pin enter the correct pin")
            main_fun()
    else:
        main_fun()
main_fun()