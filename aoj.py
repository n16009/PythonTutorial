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
    (H, W) = [int(i) for i in input().split())]
    if H == W == 0:
        break
for j in range(H):
        p = pattern[j % 2]
        print(.join([p[i % 2] for i in range(W)]))
        print()