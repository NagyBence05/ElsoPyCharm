# autoverseny
import turtle

class Auto(turtle.Turtle):
    def __init__(self,szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(15)
        self.goto(x, y)
        self.sebesseg = sebesseg

    def indit(self):
        self.forward(self.sebesseg)

ablak = turtle.Screen()
ablak.title("Autoverseny")
ablak.bgcolor("black")

a1 = Auto("red",-400, 0, 10)
a2 = Auto("green",-400, -100, 10)

ablak.listen()

ablak.onkey(turtle.bye, "Escape")
ablak.onkey(a1.indit, "d")
ablak.onkey(a2.indit, "k")

turtle.mainloop()