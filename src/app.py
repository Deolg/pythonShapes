class Form(object):
    # pylint: disable=invalid-name
    """Base class for other shapes"""
    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not x: raise Exception("x cannot be empty")
        if x != int(x): raise Exception("x must be a number")
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not y: raise Exception("y cannot be empty")
        if y != int(y): raise Exception("y must be a number")
        self._y = y

    @property
    def color(self):
        return self._y

    @color.setter
    def color(self, color):
        if not color: raise Exception("color cannot be empty")
        if color != str(color): raise Exception("color must be a number")
        self._color = color

"""
Extra class for figures with fill bgColor [Circle, Rect] 
"""
class Wrapped(object):
    def __init__(self, bgColor):
        self.bgColor = bgColor

    @property
    def bgColor(self):
        return self._bgColor

    @bgColor.setter
    def bgColor(self, bgColor):
        if not bgColor: raise Exception("bgColor cannot be empty")
        if bgColor != str(bgColor): raise Exception("bgColor must be a number")
        self._bgColor = bgColor

"""
Extra class for figures with multiple points [Broke, Rect]
"""
class Kinship(object):
    def __init__(self, points):
        self.points = points

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        if not points: raise Exception("points cannot be empty")
        error = ''

        for i in range (len(points)):
            if not len (points[i]) == 3:
                error += "array {0} wrong length need *number *number *string; ".format(points[i])
                break

            if not isinstance(points[i][0], int):
                error += " \n wrong format {0} {1} need  *number; ".format(points[i], points[i][0])

            if not isinstance(points[i][1], int):
                error += " \n wrong format {0} {1} need  *number; ".format(points[i], points[i][1])

            if not isinstance(points[i][2], str):
                error += " \n wrong format {0} {1} need  *string; ".format(points[i], points[i][2])

        if error: raise Exception(error)

        self._points = points


class Line(Form):
    def __init__(self, name, x, y, x1, y1, color):
        super().__init__(name, x, y, color)
        self.x1 = x1
        self.y1 = y1

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, x1):
        if not x1: raise Exception("x1 cannot be empty")
        self._x1 = x1

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, y1):
        if not y1: raise Exception("y1 cannot be empty")
        self._y1 = y1

    def draw(self):
        return self.name, self.x, self.y, self.x1, self.y1, self.color


class Broke(Form, Kinship):
    def __init__(self, name, x, y, color, points):
        Form.__init__(self, name, x, y, color)
        Kinship.__init__(self, points)

    def draw(self):
        return self.x, self.y, self.color, self.points

class Circle(Form, Wrapped):
    def __init__(self, name, x, y, color, bgColor, radius):
        Form.__init__(self, name, x, y, color)
        Wrapped.__init__(self, bgColor)
        self.radius = radius
    @property
    def radius(self):
        return self._y1

    @radius.setter
    def radius(self, radius):
        if not radius: raise Exception("radius cannot be empty")
        if radius != int(radius): raise Exception("the radius must be a nonnegative number")

    def draw(self):
        return self.name, self.x, self.y, self.color, self.bg_color, self.radius

class Rect(Form, Kinship, Wrapped):
    def __init__(self, name, x, y, color, bgColor, points):
        Form.__init__(self, name, x, y, color)
        Kinship.__init__(self, points)
        Wrapped.__init__(self, bgColor)

    def draw(self):
        return self.name, self.x, self.y, self.color, self.bgColor, self.points

class Canvas:
    def __init__(self):
        self.forms = []

    def call(self, form, *args):
        obj = form(*args)
        self.forms.append(form)
        print(obj.draw())

    def callAll(self):
        print(self.forms)

    def list(self):
        print(['Rect', 'Circle', 'Broke', 'Line'])


a1 = Rect('Name', 33, 43, 'color', 'bgcolor', [[32, 32, 'blue'], [43, 33, 'test']])
a2 = Rect('fdfdf', 33, 43, 'color', 'bgcolor', [[32, 32, 'blue'], [43, 33, 'test']])


#Canvas().call(Circle,'name',32,43,'red','blue', 25)
#Canvas().call(Line,'name',32,43,32,43,'red')
#Canvas().list()
#Canvas().call(Broke,'test',33,43,'color', [[21,32,'dsds'],[43,33,'green']])
#Canvas().callAll()
# Canvas().call(Rect, 'Name', 33, 43, 'color', 'bgcolor', [[32, 32, 'blue'], [43, 33, 'test']])
# Canvas().call(Rect, 'fdfdf', 33, 43, 'color', 'bgcolor', [[32, 32, 'blue'], [43, 33, 'test']])