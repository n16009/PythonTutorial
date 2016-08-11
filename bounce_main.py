from tkinter import *
import random
import time


WIDTH = 500
HEIGHT = 500
BALL_SPEED = 10
PADDLE_SPEED = 3
COLORS = ('cyan', 'green', 'gold', 'dark orange', 'magenta')
FPS = 60


class Ball:
    def __init__(self, canvas, paddle, speed, color):
        self.canvas = canvas
        self.paddle = paddle
        self.speed = speed
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, WIDTH/2,HEIGHT*0.6)
        self.x = random.choice((-3, -2, -1, 1, 2, 3))
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.canvas.bind_all('<Return>',self.start)


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] <= paddle_pos[3] and pos[1] >= paddle_pos[1]:
                return True

        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[3] >= HEIGHT:
            self.y *= -1

        if pos[3] <= 0:
            # self.y = abs(self.y) * -1
            self.hit_bottom = True

        if pos[0] <= 0:
            self.x *= -1

        if pos[2] >= WIDTH:
            self.x *= -1

        if self.hit_paddle(pos):
            self.y *= -1

    def start(self, evt):
        self.x = -self.speed
        self.y = self.speed


class Paddle:
    def __init__(self, canvas, speed, color):
        self.canvas = canvas
        self.speed = speed
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, WIDTH/2-50, HEIGHT/10)
        self.x = 0

        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -self.speed

    def turn_right(self, event):
        self.x = self.speed


class Block:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.pos_x = 50
        self.pos_y = 50
        self.id = canvas.create_rectangle(100, 0, 50, 20, fill=color, outline='white')

    def delete(self):
        self.canvas.dalete(self.id)


class Check:
    def __init__(self, block):
        self.block = block


class TextLabel:
    def __init__(self, canvas, color='green', text='GameOver!', x=250):
        self.canvas = canvas
        self.id = canvas.create_text(x, y, text=text, fill=color)

    def show(self):
        self.canvas.itemconfig(self.id, state='normal')


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
c = Canvas(tk, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
c.pack()
tk.update()

p = Paddle(c, PADDLE_SPEED, 'blue')
ball = Ball(c, p, BALL_SPEED, 'red')
blocks = []
for y in range(5):
    for x in range(9):
        blocks.append(Block(c, random.choice(COLORS)),)
print(blocks)
text = TextLabel(c)


while True:
    if not ball.hit_bottom:
        ball.draw()
        p.draw()
    else:
        text.show()

    tk.update_idletasks()
    tk.update()
    time.sleep(1/FPS)

