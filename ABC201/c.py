s = input()

ans = 0
# 書式指定記事
# https://gammasoft.jp/blog/python-string-format/#style
for i in range(10000):
    t = "{:04d}".format(i)
    ok = True
    for j in range(10):
        if s[j] == '?':
            continue
        if s[j] == 'o':
            if str(j) not in t:
                ok = False
        if s[j] == 'x':
            if str(j) in t:
                ok = False
    if ok:
        ans += 1
    
print(ans)