num = 1
def func():
    global num
    num = num + 3
    print(num)

func()
print(num)
