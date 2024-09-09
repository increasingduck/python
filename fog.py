from turtle import Turtle, exitonclick

def f1():
    a = Turtle()
    a.color("green")
    a.fillcolor("black")

    a.pensize(5)
    a.forward(50)
    a.setheading(45)
    a.forward(25)
    a.setheading(90)
    a.forward(50)
    a.left(45)
    a.forward(25)
    a.left(45)
    a.forward(50)
    a.left(90)
    a.forward(85)
    a.left(90)
    a.penright(100)
if __name__ == "__main__":
    f1()
    exitonclick()
