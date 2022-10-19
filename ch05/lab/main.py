import pygame  # Import modules

#Part A
print("\nPart A\n")
def seq(n):  # Define the function
    while n != 1:  # n not equal to 1
        print(n)
        if n % 2 == 0:        # n is even
            n = n / 2
        else:                 # n is odd
            n = (n * 3) + 1
    print(n)                  # the last output is 1



seq(101)    # run the sequence for the integer 101

#Part B
print("\nPart B\n")


def seqcnt(n):  # Define iteration function
    count = 0
    while n != 1:  # Iteration loop while n is not equal to 1
        count +=1
        #print(n)
        if n % 2 == 0:        # n is even
            n = n / 2
        else:                 # n is odd
            n = (n * 3) + 1
    print(n);                 # print the value after each iteration
    print("\nNumber of iterations: ", count)    # after loop is finished, print count
    print("\n")
    return(count) # send the number of iterations back to main program

# - - - - Part B main program - - - -

upper_limit = 100   # maximum number to iterate
iters = {}          # dictionary to store pairs of integer and # of iterations on that integer
max_so_far = 0      # Keep track of greatest # of iterations as we sweep through range (added for Part C)

for i in range (2, upper_limit + 1):     # Begin calling iteration function for each number in the range, inclusive
    print("Testing: ", i)
    result = seqcnt(i)
    iters[i] = result
    if iters[i] > max_so_far:       # Keep track of the greatest # of iterations
        max_so_far = iters[i]
#print(iters)
print("Max # of iterations during this run = ", max_so_far)

#Part C
print("\nPart C\n")

red = (255, 0, 0)       # Line color of # of interations (Y) vs integer value (X)
bgcolor = (0, 180, 180) # Background color of screen
black = (0, 0, 0)       # Text color



pygame.init()           # Initialize pygame

#MAKING THE GRAPH...GRAPHS THE INTERGERS THAT GETS ITERATED AFTER ALL OF THEM IS ITERATED BUT NEED TO GRAPH AFTER EACH INETERGER IS ITERATED.

display = pygame.display.set_mode((600,500)) # Open the output window
pygame.display.set_caption("Iteration Data for 3n+1, where n = 2 to " + str(upper_limit))  #Name the window
display.fill(bgcolor)       # Window background
pygame.display.update()




xy = list(zip(iters.keys(), iters.values())) # Build list of coordinate pairs.
#print(xy)
print("Number of coordinate pairs = ", len(xy))
if len(xy) >= 2:    # Make sure we have at least 2 pair of coordinates to draw line segment
    pygame.draw.lines(display, red, False, xy)  # Plot the data. X = integer, Y = iterations
    new_display = pygame.transform.flip(display, False, True)   #flip graph on vertical axis
    display.blit(new_display , (0, -50))        # offset lines a little
    pygame.display.update()



font = pygame.font.Font(None, 26)  # configure the font as system default


#CREATING TITLE ON GRAPH 
iterationTextMsg = font.render("Maximum number of iterations is: ", 1, black)   # Create the message string
iterationNumericMsg = font.render(str(max_so_far), 1, black)    # Numeric part has to be expressed as a string



display.blit(iterationTextMsg, (20, 20))        # draw the screen message and max number of iterations      
display.blit(iterationNumericMsg, (310, 20))
pygame.display.update()


#
print("\nPress any key to exit the program.")



# Keep program from exiting abruptly
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # Exit if user presses a key
            run = False
pygame.quit()