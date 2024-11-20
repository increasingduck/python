from turtle import * 
from random import randint, choice

############# DEFINE CLASSES AND FUNCTIONS #############
def road():
    r = Turtle()
    r.hideturtle()
    r.speed(0)
    r.goto(-160,500)
    r.fillcolor("gray")
    r.begin_fill()
    r.goto(160,500)
    r.goto(160,-500)
    r.goto(-160,-500)
    r.end_fill()

class Car(Turtle):
    '''
    ConstructorS
    '''
    def __init__(self, shape, x, y):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.setheading(270)

    '''
    drive() Method
    '''
    def drive(self):
        self.forward(10)
    '''
    relocate() Method
    '''
    def relocate(self):
        if self.ycor() < -300:
            self.goto(randint(-150, 150), 300)
    
    def collide(self, player):
        dist5q = (self.xcor() - player.xcor()) ** 2 + (self.ycor() - player.ycor()) ** 2
        dist = dist5q ** 0.5


        if dist < 20:
            print("collide")
            return True
        return False




class Player(Turtle):

    def __init__(self, shape, x, y):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)

        self.screen.onkeypress(self.go_right, 'd' )
        self.screen.onkeypress(self.go_left, 'a' )
        self.screen.listen()

    def go_right(self):
        print("right")
        #self.setheading(0)
        #self.forward(10)
        self.goto(self.xcor()+10, self.ycor())


    def go_left(self):
        print("left")
        #self.setheading(180)
        #self.forward(10)
        self.goto(self.xcor()-10, self.ycor())




############# YOUR PROGRAM  #############
screen = Screen()
screen.tracer(0)
screen.bgcolor("green")
road()
screen.register_shape("one.gif")
screen.register_shape("two.gif")
screen.register_shape("three.gif")
screen.register_shape("four.gif")
screen.register_shape("five.gif")
screen.tracer(1)

images = ["one.gif", "two.gif", "three.gif", "four.gif", "five.gif"]

#c = Car("one.gif", 100, 100)
#d = Car("two.gif", 10, 10)

cars = []
for i in range(5):
    temp = Car(images[i], randint(-150, 150), randint(300,300))
    cars.append(temp)

player = Player("one.gif", 0, 0)

print(cars)

running = True
while running:
    for car in cars:
        car.drive()
        car.relocate()
        if car.collide(player):
            running = False
            break




screen.mainloop()