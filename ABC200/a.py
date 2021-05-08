n = int(input())
rsl = n // 100
if n == rsl*100:
    print(rsl)
else:
    print(rsl+1)