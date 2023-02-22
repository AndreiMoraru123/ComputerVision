import matplotlib.pyplot as plt

'''
The color class creates a color from 3 values, r, g, and b (red, green, and blue).

attributes:
    r - a value between 0-255 for red
    g - a value between 0-255 for green
    b - a value between 0-255 for blue
'''


class Color(object):

    # __init__ is called when a color is constructed using color.Color(_, _, _)
    def __init__(self, r, g, b):
        # Setting the r value
        self.r = r

        ## TODO: Set the other two color variables g and b
        ## Hint: use the same format as the r variable

        # Setting the g value
        self.g = g

        # Setting the b value
        self.b = b

    # __repr__ is called when a color is printed using print(some_color)
    # It must return a string
    def __repr__(self):
        '''Display a color swatch and then return a text description of r,g,b values.'''

        plt.imshow([[(self.r / 255, self.g / 255, self.b / 255)]])

        ## TODO: Write a string representation for the color
        ## ex. "rgb = [self.r, self.g, self.b]"
        ## Right now this returns an empty string
        string = "rgb = [" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + "]"
        return string

    def __add__(self, other):
        '''Adds the r, g, and b components of each color together
           and averaging them.
           The new Color object, with these averaged rgb values,
           is returned.'''

        r = (self.r + other.r) / 2
        g = (self.g + other.g) / 2
        b = (self.b + other.b) / 2

        return Color(r, g, b)
