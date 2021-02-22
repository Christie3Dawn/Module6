class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x,self.y)


class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def create_rectangle(x,y,width,height):
    posn = Point(x,y)
    rect =  Rectangle(posn,width,height)
    return rect

def str_rectangle(rect):
    return rect.__str__()

def shift_rectangle(rect, dx, dy ):
    rect.corner.x = rect.corner.x + dx
    rect.corner.y += dy


def offset_rectangle(rect, dx, dy):
    return create_rectangle(rect.corner.x + dx, rect.corner.y + dy, rect.width, rect.height)


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

r1 = create_rectangle(10, 20, 30, 40)
print( str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print( str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print( str_rectangle(r1))  # should be same as previous
print( str_rectangle(r2))

