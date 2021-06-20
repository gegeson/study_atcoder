n = int(input())

day = 0
res = 0
while True:
    day += 1
    res += day
    if res >= n:
        print(day)
        exit()
    