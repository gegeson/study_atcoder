import string

p = list(map(int, input().split()))

ans = []
for i in range(len(p)):
    ans.append(string.ascii_lowercase[p[i] - 1])
print("".join(ans))
