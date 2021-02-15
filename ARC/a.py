T = int(input())

for t in range(T):
    l, r = map(int, input().split())
    # for i in range(l*2,r+1):
    #     ans += i + 1 - l * 2
    # print(ans)
    if l * 2 <= r:
        start = 1
        end = r - l*2 + 1
        ans = int((start + end) * (end - start + 1) / 2)
        print(ans)
    else:
        print(0)