#import modules
import turtle 

width = 500 #setting up the screen
height = 700
window = turtle.Screen() 
tree = turtle.Turtle()
window.setup(width, height)
window.title("Happy (early) Holidays!")
tree.color("green")
window.bgcolor("red")

#Creating the tree trunk
trunk = turtle.Turtle()
trunk.color("chocolate")
trunk.right(90)
trunk.pensize(60)
trunk.up()
trunk.forward(100)
trunk.down()
trunk.forward(300)

#Creating Tree Branches Using Tuples

tree_positions = ((50, 40), (100, 20), (140, -10), (160, -40))
#x-coordinate is the length of the branch
#y-position is the y-value for top of the branch (triangle) being drawn

def tree_branch(size, y_position): 
  '''
  Draws the branches on the Christmas tree
  size: (int) Horizontal length of branches 
  y_position: (int) y-value of top of branch
  no return
  '''
  tree.begin_fill()
  tree.setpos(0, y_position)
  tree.setpos(size, y_position-size)
  tree.setpos(-size, y_position-size)
  tree.setpos(0, y_position)
  tree.end_fill()


#Function used to choose star color
def userchoice():
    '''
Ask user to choose from three options for the star's color.
Verify that one of the choices was selected and if an error was made, use gold as the default color. Demonstrates a function that returns a value.
ret - colorchoice: (string) The user's color choice.
    '''

    colorchoice = input("What color star would you like on your tree, gold, silver, or violet? ")
    if colorchoice == "gold" or colorchoice == "silver" or colorchoice == "violet":
      return(colorchoice)
    else:
      print("An error has occurred, ", colorchoice, "is not a valid choice.  Using gold by default.")
      return("gold") # If the user fails to make a valid choice, use gold as the default color.
     
# Function for Star
def drawstar(starcolor):
  '''
  Draw the star on Christmas tree
  starcolor: (string) color of star
  no return
  '''
  star = turtle.Turtle()

# Length of side of the star
  starlen = 30 

# Fill color of star
  star.up()
  star.setpos(15, 70)
  star.fillcolor(starcolor)

# Start filling star
  star.begin_fill()

  star.right(12) # Place star evenly on tree
  for _ in range(5): # Star has 5 points 
        star.forward(starlen) # draw the points on the star
        star.right(120)
        star.forward(starlen)
        star.right(-48)

# Stop filling the star and hide the turtle cursor
  star.end_fill()
  star.hideturtle()

def main():
  # Create branches on Christmas tree
  for (size, y_position) in tree_positions:
    tree_branch(size, y_position)
    
# Ask the user to choose a color for the star for top of the tree
  starcolor = userchoice()

# Draw the star with user's color
  drawstar(starcolor)

main()

window.exitonclick()