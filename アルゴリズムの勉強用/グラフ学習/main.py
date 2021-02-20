from urllib import request
import matplotlib.pyplot as plt
# matplotlib inline

url = 'https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/location.txt'
# 指定したURLからリソースをダウンロードし、名前をつける。
request.urlretrieve(url, '/Users/gege/python-programing/study_atcoder/アルゴリズムの勉強用/グラフ学習/location.txt')

# ダウンロードしたデータから、列ごとに数字を読み込んでリストに格納する。
col1 = []
col2 = []
col3 = []
for i, line in enumerate(open('/Users/gege/python-programing/study_atcoder/アルゴリズムの勉強用/グラフ学習/location.txt')):
    if i == 0:
        continue
    c = line.split(",")
    col1.append(c[0])
    col2.append(float(c[1]))
    col3.append(float(c[2]))
    
# print(col1)
# print(col2)
# print(col3)

# グラフ作成
plt.figure(figsize=(10,8))
plt.scatter(col3, col2, alpha=0.5)
plt.title("Prefectural capitals in Japan")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
for city, x, y in zip(col1, col3, col2):
    plt.text(x, y, '', alpha=0.5, size=12)
    # 文字表示するときは
    # plt.text(x, y, city, alpha=0.5, size=12)
plt.show()    