n = int(input())
a = list(list(map(int, input().split())))
b = list(list(map(int, input().split())))

cnt = min(b) - max(a) + 1

if cnt <= 0:
    print(0)
    exit()
print(cnt)