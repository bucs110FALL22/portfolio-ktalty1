import turtle

CIRCLE_DEG = 360
screen = turtle.Screen()


sides = int(input("Please enter the number of sides: "))

length = int(input("Please enter the length of each side: "))

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
angle = 360 / sides

for i in range(sides):
  my_turtle.forward(length)
  my_turtle.left(angle)
   

screen.exitonclick()
