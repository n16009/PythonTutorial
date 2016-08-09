data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for文を使って合計を求める
total = 0
for i in data:
    total += i

print(total)

# dataの中から偶数だけを表示する
for a in data:
    if a % 2 == 0:
        print(a)

