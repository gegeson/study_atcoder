x = int(input())

num = 100
while True:
    if x > num:
        num += 100
    elif x == num:
        print(100)
        break
    else:
        print(num - x)
        break
    