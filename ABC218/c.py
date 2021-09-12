n = int(input())
s = list(list(input()) for _ in range(n))
t = list(list(input()) for _ in range(n))


def rool(arr):
    return [i[::-1] for i in zip(*arr)]


for _ in range(4):
    s = rool(s)
    while True:
        if "#" not in s[0]:
            s.pop(0)
        else:
            break

for _ in range(4):
    t = rool(t)
    while True:
        if "#" not in t[0]:
            t.pop(0)
        else:
            break

for _ in range(4):
    s = rool(s)
    if s == t:
        print("Yes")
        exit()

print("No")

