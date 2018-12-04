import tkinter
import random

class RandomBall():
    def __init__(self, canvas, screenwidth, screenheight):
        self.canvas = canvas
        self.xpos = random.randint(10, int(screenwidth) - 20)
        self.ypos = random.randint(10, int(screenheight) - 20)
        self.xspeed = random.randint(8, 20);
        self.yspeed = random.randint(8, 20);
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.radius = random.randint(20, 120)
        color = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (color(), color(), color())

    def create_ball(self):
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.item = self.canvas.create_oval(x1, y1, x2, y2, \
                                            fill=self.color, \
                                            outline=self.color)

    def move_ball(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed

        if self.xpos + self.radius >= self.screenwidth or \
                self.xpos - self.radius <= 0:
            self.xspeed = -self.xspeed

        if self.ypos + self.radius >= self.screenheight or \
                self.ypos - self.radius <= 0:
            self.yspeed = -self.yspeed

        self.canvas.move(self.item, self.xspeed, self.yspeed)


class ScreenSaver():
    def __init__(self):
        self.balls = []
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        self.root.overrideredirect(1)
        self.root.attributes('-alpha', 0.4)

        self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Key>', self.myquit)
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, screenwidth=w, screenheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        self.canvas.after(50, self.run_screen_saver)

    def myquit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    ScreenSaver()

