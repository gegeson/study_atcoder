s = list(input())
t = list(input())

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        s[i], s[i + 1] = s[i + 1], s[i]
        if s == t:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

print("Yes")

