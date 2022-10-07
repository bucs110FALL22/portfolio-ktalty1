import pygame  # Import modules
import random
import math

# PART A  

blue = (30,144, 255)    # RGB for window background
pink = (255, 174, 201)  # Dartboard wood
black = (0, 0, 0)   # Lines
green = (0, 255, 0) #Dart Hits
red = (255, 0, 0) #Dart Misses
white = (255, 255, 255) #White team/dart hits


pygame.init()
window = pygame.display.set_mode((400,400)) # Open the game window
pygame.display.set_caption("Dart Game")  #Name the window


window.fill(blue) # Screen background
pygame.draw.circle(window, pink,(200,200),200)  
pygame.draw.line(window,black,(0,200),(400,200)) # Horizontal line
pygame.draw.line(window,black,(200,0),(200,400)) # Vertical line

pygame.display.update()
pygame.time.wait(800)

# PART B

dart_x = random.randrange(400)
dart_y = random.randrange(400)
distance_from_center = math.hypot(200 - dart_x, 200 - dart_y)
is_in_circle = distance_from_center <= 200

for i in range (0, 10):
  dart_x = random.randrange(400)
  dart_y = random.randrange(400)
  distance_from_center = math.hypot(200 - dart_x, 200 - 
  dart_y)
  is_in_circle = distance_from_center <= 200
  if is_in_circle == True:
    dart_color = green
  else: 
    dart_color = red
  pygame.draw.circle(window, dart_color, (dart_x, 
  dart_y), 7)
  pygame.display.update()
  pygame.time.wait(700)

pygame.time.wait(500)

#Part C
window = pygame.display.set_mode((400,400)) # Open the game window
window.fill(blue) # Screen background
pygame.draw.rect(window, green, pygame.Rect(50,150,100,100))    # Add green player rectangle
pygame.draw.rect(window, white, pygame.Rect(250,150,100,100))   # Add white player rectangle
pygame.display.update()



print("")
print("Who will win the dart game?")
print("The green player or the white player?")
print("Click on the rectangle of your choice!")
print("")



exit_event = False
  
# Creating a loop to watch for a mouse click
while not exit_event:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # Click event
            if event.button == 1:
                #print("Mouse coordinates = ", event.pos)
                if (event.pos[0] >= 50 and event.pos[0] <= 150 and event.pos[1] >= 150 and event.pos[1] <= 250) or (event.pos[0] >= 250 and event.pos[0] <= 350 and event.pos[1] >= 150 and event.pos[1] <= 250): # Make sure the user clicked inside a rectangle
                    exit_event = True # Mouse clicked, coordinates captured, exit loop



mouse_pos = event.pos # Friendlier name



#print(mouse_pos[0], mouse_pos[1])



pick_team = False
while not pick_team:
    if mouse_pos[0] >= 50 and mouse_pos[0] <= 150 and mouse_pos[1] >= 150 and mouse_pos[1] <= 250:
        print("Good luck with the green player")
        pick_team = 1
    elif mouse_pos[0] >= 250 and mouse_pos[0] <= 350 and mouse_pos[1] >= 150 and mouse_pos[1] <= 250:
        print("Good luck with the white player")
        pick_team = 2



#print(pick_team)



# Set up dart board again for two-player game
pygame.draw.circle(window, pink,(200,200),200)   # Draw the dartboard w/crosshairs
pygame.draw.line(window,black,(0,200),(400,200)) # Horizontal line
pygame.draw.line(window,black,(200,0),(200,400)) # Vertical line



pygame.display.update()
green_score = 0
white_score = 0



for c in range (0, 10):     # Begin the dart game with 10 rounds
    dart_x = random.randrange(400)  # green player throws a dart
    dart_y = random.randrange(400)
    distance_from_center = math.hypot(200 - dart_x, 200 - dart_y)
    is_in_circle = distance_from_center <= 200
    if is_in_circle == True:
        dart_color = green
        green_score +=1
    else:
        dart_color = red
    pygame.draw.circle(window, dart_color,(dart_x,dart_y),6)
    pygame.display.update()
    pygame.time.wait(500)

    dart_x = random.randrange(400)  # white player throws a dart
    dart_y = random.randrange(400)
    distance_from_center = math.hypot(200 - dart_x, 200 - dart_y)
    is_in_circle = distance_from_center <= 200
    if is_in_circle == True:
        dart_color = white
        white_score +=1
    else:
        dart_color = black
    pygame.draw.circle(window, dart_color,(dart_x,dart_y),6)
    pygame.display.update()
    pygame.time.wait(500)



print("")
print("*** Final score ***")
print("Green player: ", green_score)
print("White player: ", white_score)
print("")



if green_score > white_score:
    print("The green player has won")
    if pick_team == 1:       # User chose the green player to win
        print("Congratulation! Your player won!")
    else:
        print("Your player didn't win.  Better luck next time!")
elif white_score > green_score:
    print("The white player has won")
    if pick_team == 2:       # User chose the white player to win
        print("Congratulation! Your player won!")
    else:
            print("Your player didn't win.  Better luck next time!")
else:
    print("The game has ended in a tie")


pygame.time.wait(10000) #Keep dartboard and score visible for 10 seconds