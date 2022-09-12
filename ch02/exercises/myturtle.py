import turtle

CIRCLE_DEG = 360
window = turtle.Screen()


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
sides = 4
length = 50
my_turtle.color("purple")
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)
my_turtle.forward(length)
my_turtle.left(360 / sides)

my_turtle.up()
my_turtle.forward(100)
my_turtle.down()

my_turtle.color("red")
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)
my_turtle.forward(length)
my_turtle.left(CIRCLE_DEG / sides)

window.exitonclick()