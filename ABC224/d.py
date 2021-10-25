m = int(input())

hashmap = {}
for i in range(m):
    a, b = map(str, input().split())
    if a in hashmap:
        hashmap[a].append(b)
    else:
        hashmap[a] = list(b)

p = list(map(int, input().split()))

