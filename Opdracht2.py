import numpy as np

def draw_mandel(width : int):
    """Draws mandel
    
    :param width: determs the width and height of the picture
    """
    #width = height
    #x range [-1.5; 0.5]
    #y range [-1; 1]
    #diverging index (n) determs the pixel colour. Black if n = 0. Otherwise some white or blue

def create_mandel() -> np.array:
    """Creates the mandel points
    
    :return:
        numpy array: contains all points of the mandel
    """
    #a[0] = 0
    #a[n] = a[n-1]**2 + complex(x,y)
    #if |a[n]| > 2 is n the diverging index. if n not between 0 en 100 -> 0
    c = complex([-1.5, 0.5], [-1, 1])

create_mandel()