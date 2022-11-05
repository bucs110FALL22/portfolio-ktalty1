from Rectangle import Rectangle


class Surface:  #Creating the class

    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def __getRect__(self):
        return {self.rect}
