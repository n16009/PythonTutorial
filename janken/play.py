import random

def you_hand():
    while True:
        print("あなたの手 : "),
        hand = int(input())
        if hand == 1 or hand == 2 or hand == 3: break
        print("1~3の数字を入力してください")
    return hand


def check_hand(y, c):
    if y == c:
        if y == 1: print("共にグーで",)
        if y == 2: print("共にチョキで",)
        if y == 3: print("共にパーで",)
        print("引き分けです")
        return 0
    else:
        if y == 1:
            if c == 2:
                print("あなた:グー, COM:チョキ...YOU WIN!!")
                return 1
            if c == 3:
                print("あなた:グー, COM:パー...YOU LOSE!!")
                return -1
        if y == 2:
            if c == 1:
                print("あなた:チョキ, COM:グー...YOU LOSE!!")
                return -1
            if c == 3:
                print("あなた:チョキ, COM:パー...YOU WIN!!")
                return 1
        if y == 3:
            if c == 1:
                print("あなた:パー, COM:グー...YOU WIN!!")
                return 1
            if c == 2:
                print("あなた:パー, COM:チョキ...YOU LOSE!!")
                return -1
def calc_rate(d, w, a):
    if a == d: p = 0
    else: p = w / (a - d)
    return p

# def save_score(result):


if __name__ == "__main__":
    draw, win, all = 0.0, 0.0, 0.0
    print("じゃんけんゲームスタート")
    print("グー:1 ,チョキ:2 ,パー:3を入力してください")
    while True:
        p = calc_rate(draw, win, all)
        you = you_hand()
        com = random.randint(1, 3)
        tmp = check_hand(you, com)
        if tmp == 0: draw += 1
        if tmp == 1: win += 1
        again = input()


     # コンピュータの手と勝敗の結果を表示
     #  save_score(result)
