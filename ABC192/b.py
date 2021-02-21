s = str(input())

for i in range(len(s)):
    if i % 2 == 0:
        if s[i].isupper():
            print('No')
            exit()
    elif i % 2 == 1:
        if s[i].islower():
            print('No')
            exit()
print('Yes')
    