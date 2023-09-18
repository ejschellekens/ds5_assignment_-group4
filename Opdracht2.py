from PIL import Image, ImageDraw

def draw_mandel(width : int):
    """Draws mandel
    
    :param width: determs the width and height of the picture
    """
    im = Image.new('RGB', (width, width), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, width):
        for y in range(0, width):
            c = pixelToC(x, width, y)
            a = create_mandel(c)
            
            color = 255 - int(a * 255 / 80)

            draw.point([x, y], (color, color, color))

    im.save('output.png', 'PNG')

def create_mandel(c: complex) -> int:
    """Creates the mandel point
    
    :param c: the complex number added to z
    :return:
        n: number of iters for z to get to 2
    """
    MAX_ITER = 80

    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def pixelToC(x: int, width : int, y: int) -> complex:
    """Turns pixel into a complex number
    
    :param x: x coordinate
    :param width: amount of pixels
    :param y: y coordinate
    :return:
        c: the complex number of the pixel
    """
    c = complex(-1.5 + (x / width) * (0.5 + 1.5), -1 + (y / width) * (1 + 1))
    return c

draw_mandel(200)