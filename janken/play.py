import random

HANDS = ['グー', 'チョキ', 'パー']


def select_hand():
    while True:
        print("あなたの手"),
        HANDS = input()
        if HANDS == 1 or HANDS == 2 or HANDS == 3: break
    return 0


def judgement():
    if player == computer:
        if player == 1: print("共にグーで"),
        if player == 2: print("共にチョキで"),
        if player == 3: print("共にパーで"),
        print("引き分け")
        return HANDS
    else:
        if player == '1':
            if computer == '2':
                print("あなた:グー, COM:チョキ...あなたの勝ち!!")
                return +1
            if computer == '3':
                print("あなた:グー, COM:パー...あなたの負け!!")
                return -1
        if player == '2':
            if computer == '1':
                print("あなた:チョキ, COM:グー...あなたの負け!!")
                return -1
            if computer =='3':
                print("あなた:チョキ, COM:パー...あなたの勝ち!!")
                return +1
        if player == '3':
            if computer == '1':
                print("あなた:パー, COM:グー...あなたの勝ち!!")
                return +1
            if computer == '2':
                print("あなた:パー, COM:チョキ...あなたの負け!!")
                return -1


"""
じゃんけんの勝敗を判定する。
:param player: HANDSの中のどれか。
:param computer: HANDSの中のどれか。
:return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す。
"""
pass


def save_score(result):
    """
    'score.txt'に戦績を保存。
    wintx lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    """
    pass


def calc_rate(d, w, a):
    if a == d: p = 0
    else: p = w / (a - d)
    return p


if __name__ == '__main__':
    draw, win, all = 0.0, 0.0, 0.0
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = random.randint(1, 3)
    result = judgement()
    while True:
        p = calc_rate(draw, win, all)
        com = random.randint(1, 3)
        tmp = judgement()
        if tmp == 0: draw += 1
        if tmp == 1: win += 1
        again = input()


     # コンピュータの手と勝敗の結果を表示
    save_score(result)
