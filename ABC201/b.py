n = int(input())

st_list = []
for i in range(n):
    s, t = input().split()
    st_list.append([int(t),s])

st_list.sort(reverse=True)
print(st_list[1][1])

