# a, b = [int(i) for i in input().split()]
#W, H, x, y, r = [int(i) for i in input().split()]

#data = [int(i) for i in input().split()]

#data,.ort()
#print("{0}{1}{2}".format(data[0],data[1],data[2]))

#def main():
#    print ([int(i) for i in input("Hello World\n").split(1000)])

#if __name__ == '__main__':
#    main()
"""
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
"""

def solve(n, m, a, b):
    res = []
    for i in range(n):
        s = [a[i][j] * b[j] for j in range(m)]
        res.append(sum(s))
    return res

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    a = [[int(i) for i in input().split()] for _ in range(n)]
    b = [for i in input()] for _ in range(m)]
    for x in solve(n, m, a, b):
        print(x)