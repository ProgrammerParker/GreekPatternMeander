import turtle
screen = turtle.Screen()
screen.bgcolor("orange")

myTurtle=turtle.Turtle()
myTurtle.color("white")
myTurtle.pensize(5)
myTurtle.pencolor("black")
myTurtle.hideturtle()
myTurtle.speed(20)

size=10

for i in range(100):
        myTurtle.forward(size)
        myTurtle.right(125)
        size+=10

turtle.exitclick()
