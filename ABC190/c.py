import itertools

# 1<=k<=16だから全探索で回せる

n, m = map(int, input().split())

cond = [tuple(map(int, input().split())) for i in range(m)]
k = int(input())
choice = [tuple(map(int, input().split())) for i in range(k)] 
ans = 0
# itertools.productはballsの全ての可能性を炙り出したもの
for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(a in balls and b in balls for a, b in cond)
    if ans < cnt:
        ans = cnt

print(ans)