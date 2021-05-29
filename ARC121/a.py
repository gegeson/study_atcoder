import itertools

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
x_copy = x.copy()
y_copy = y.copy()
x_copy.sort()
y_copy.sort()

# これだと一番目のものと同じ組のものが２番になる可能性がある
# dis_x1 = abs(x[0] - x[-1])
# dis_x2 = abs(x[0] - x[-2])
# dis_x3 = abs(x[1] - x[-1])
# dis_y1 = abs(y[0] - y[-1])
# dis_y2 = abs(y[0] - y[-2])
# dis_y3 = abs(y[1] - y[-1])


# dis_list = [dis_x1, dis_x2, dis_x3, dis_y1, dis_y2, dis_y3]
# dis_list.sort()
# print(dis_list[-2])

index = []
for i in range(n):
    if x[i] == x_copy[0]:
        index.append(i)
    elif x[i] == x_copy[-1]:
        index.append(i)
    elif x[i] == x_copy[-2]:
        index.append(i)
    elif x[i] == x_copy[1]:
        index.append(i)
    elif y[i] == y_copy[-1]:
        index.append(i)
    elif y[i] == y_copy[0]:
        index.append(i)
    elif y[i] == y_copy[-1]:
        index.append(i)
    elif y[i] == y_copy[-2]:
        index.append(i)
    elif y[i] == y_copy[1]:
        index.append(i)

dis_list = []
for i in itertools.combinations(index,2):
    dis_x = abs(x[i[0]] - x[i[1]])
    dis_y = abs(y[i[0]] - y[i[1]])
    dis = max(dis_x, dis_y)
    dis_list.append(dis)

dis_list.sort()
print(dis_list[-2])