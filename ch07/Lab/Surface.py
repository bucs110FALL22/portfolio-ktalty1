from Rectangle import Rectangle


class Surface:  #Creating the class

    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.rect = Rectangle(x, y, h, w)
'''
This function created a rectangle object based on (x, y) coordinates and the w and h values. Also saves filename as a parameter to self.image instance variable.
	x: (int) x-coordinate of upper left position
  y: (int) y-coordinate of upper left position
  w: (int) width of rectangle
  h: (int) height of rectangle
  filename: (str) name of file
	No return

Noticed that height and width are switched between different methods in Rectangle class. 
'''
def __getRect__(self):
      return {self.rect}
