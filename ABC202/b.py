s = input()

a = ''
for i in range(len(s)):
    if s[i] == '6':
        a = a + '9'
    elif s[i] == '9':
        a = a + '6'
    else:
        a = a + s[i]

print(a[::-1])