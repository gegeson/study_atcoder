n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x_diff1 = point[i][0] - point[j][0]
            x_diff2 = point[j][0] - point[k][0]
            x_diff3 = point[k][0] - point[i][0]

            y_diff1 = point[i][1] - point[j][1]
            y_diff2 = point[j][1] - point[k][1]
            y_diff3 = point[k][1] - point[i][1]

            if x_diff1 == x_diff2 == x_diff3 or y_diff1 == y_diff2 == y_diff3:
                continue

            if x_diff1 != 0 and x_diff2 != 0:
                xy1 = float(y_diff1 / x_diff1)
                xy2 = float(y_diff2 / x_diff2)
            elif x_diff2 != 0 and x_diff3 != 0:
                xy1 = float(y_diff2 / x_diff2)
                xy2 = float(y_diff3 / x_diff3)
            elif x_diff1 != 0 and x_diff3 != 0:
                xy1 = float(y_diff1 / x_diff1)
                xy2 = float(y_diff3 / x_diff3)

            if xy1 == xy2:
                continue
            else:
                count += 1
print(count)
