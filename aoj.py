"""
# a, b = [int(i) for i in input().split()]
#W, H, x, y, r = [int(i) for i in input().split()]

#data = [int(i) for i in input().split()]

#data,.ort()
#print("{0}{1}{2}".format(data[0],data[1],data[2]))

#def main():
#    print ([int(i) for i in input("Hello World\n").split(1000)])

#if __name__ == '__main__':
#    main()

while True:
    a, op, b = input().sprit()
    a = int(a)
    b = int(b)

    if op == '?':
        break

    if op == '+':
        print(a + b)

    if op == '-':
        print(a - b)

    if op == '*':
        print(a * b)

    if op == '/':
        print(a / b)



count = input()
data = [int(i) for i in input().split()]

print(min(data), max(data), sum(data))



pattern = {
    0: ["#", "."],
    1: [".", "#"],
}

while True:
    (H, W) = [int(i) for i in input().split()]
    if H == W == 0:
        break
for j in range(H):
        p = pattern[j % 2]
        print("join([p[i % 2] for i in range(W)])")
        print()

while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break

    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')

        print()
    print()


data = [
    "{0} {1}".format(s, r)
    for s in ('S', 'H', 'C', 'D')
    for r in range(1, 13 + 1)
    ]

count = int(input())
for c in range(count):
    card = input()
    data.remove(card)

for c in data:
    print(c)


data = [
    [[0 for r in range(10)] for f in range(3)] for b in range(4)
]

# 入力データ読み込んで処理をここから書いていく
count = int(input())
for c in range(count):
    b, f, r, v = [int(i) for i in input().split()]
    data[b-1][f-1][r-1] += v

for bi, b in enumerate(data):
    for f in b:
        for r in f:
            print(' {0}'.format(r), end='')

        print()
    if bi < 3:
        print('#' * 20)



n, m = [int(i) for i in input().split()]

matrix = []
for ni in range(n):
    matrix.append([int(a) for a in input().split()])

vector = []
for mi in range(m):
    vector.append(int(input()))

for ni in range(n):
    sum = 0
    for mi in range(m):
        sum += matrix[ni][mi] * vector[mi]

    print(sum)


while True:
    m, f, r = [int(i) for i in input().split()]

    if m == f == r == -1:
        break

    total = m + f
    if m == -1 or f == -1 or total < 30:
        print('F')

    elif total < 50 and r < 50:
        print('D')

    elif total < 65:
        print('C')

    elif total < 80:
        print('B')

    else:
        print('A')



while True:
    n, x = [int(i) for i in input().split()]

    if n == x == 0:
        break

    count = 0
    for s in range(1, n - 1):
        for m in range(s + 1, n):
            for e in range(m + 1, n + 1):
                if x == sum([s, m, e]):
                    count += 1

    print(count)


r, c = [int(i) for i in input().split()]

data = []
sum_row = [0] * (c + 1)

for ri in range(r):
    data.append([int(i) for i in input().split()])
    data[ri].append(sum(data[ri]))
    print(" ".join([str(d) for d in data[ri]]))
    for ci in range(c + 1):
        sum_row[ci] += data[ri][ci]

print(" ".join([str(s) for s in sum_row]))



n, m, l = [int(i) for i in input().split()]

A = []
B = []
C = []

for ni in range(n):
    A.append([int(i) for i in input().split()])

for mi in range(m):
    B.append([int(i) for i in input().split()])

for i in range(n):
    C.append([])
    for j in range(l):
        C[i].append(0)
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for li in range(n):
    print(" ".join([str(s) for s in C[li]]))


while True:
    data = input()
    if data[0] == '0':
        break

    print(sum([int(i) for i in data]))

    for integer, numeral in self.known_values:
            result = roman1.to_roman(integer)
            self.assertEqual(numeral, result)

"""

