import numpy as np
from PIL import Image as im
from matplotlib import pyplot as plt

def draw_mandel(width : int):
    """Draws mandel
    
    :param width: determs the width and height of the picture
    """
    #width = height
    #x range [-1.5; 0.5]
    #y range [-1; 1]
    #diverging index (n) determs the pixel colour. Black if n = 0. Otherwise some white or blue
    c = pixelToC(width)
    a = create_mandel(c)
    
    


def create_mandel(c : np.array) -> np.array:
    """Creates the mandel points
    
    :return:
        numpy array: contains all points of the mandel
    """
    #a[0] = 0
    #a[n] = a[n-1]**2 + c
    #if |a[n]| > 2 is n the diverging index. if n not between 0 en 100 -> 0
    a = [0]
    index = 1
    for i in c:
        uitkomst = a[index-1]**2 + i
        if abs(uitkomst) > 2:
            a.append(uitkomst)
        else:
            a.append(0)

    a = np.array(a)
    return a

def pixelToC(width : int) -> np.array:
    """Turns pixels into a complex number
    
    :param width: amount of pixels
    :return:
        numpy array: all the complex numbers in the pixel grid 
    """
    c = []
    height = width
    for x in range(width):
        for y in range(height):
            c.append(complex(x,y))

    c = np.array(c)

    return c

draw_mandel(200)