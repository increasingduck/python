def road():
    r = Turtle()
    r.hideturtle()
    r.speed(0)
    r.goto(-160,500)
    r.fillcolor("gray")
    r.begin_fill()
    r.goto(160,-500)
    r.goto(-160,-500)
    r.end_fill()

class Player(turtle):
    def __init__(self, shape, x, y):
        super().__init__()
    self.shape(car)
    self.penup()
    self.goto(x, y)

class Planes(cars):



class Passengers():