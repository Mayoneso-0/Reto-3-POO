import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: "Point" = None, end: "Point" = None
                 , length: float = 0, slope: float = 0):
        self.start = start
        self.end = end
        self.length = length
        self.slope = slope
    def compute_length(self):
        length = ((self.start.x - self.end.x)**2 
                  + (self.start.y - self.end.y)**2)**0.5
        return length
    def compute_slope(self):
        slope = math.atan2((self.end.y - self.start.y),
                           (self.end.x - self.start.x)) * 180 / math.pi
        return slope
    def compute_horizontal_cross(self):
        if self.start.y <= 0 and self.end.y >= 0:
            return True
        elif self.start.y >= 0 and self.end.y <= 0:
            return True
        else:
            return False
    def compute_vertical_cross(self):
        if self.start.x <= 0 and self.end.x >= 0:
            return True
        elif self.start.x >= 0 and self.end.x <= 0:
            return True
        else:
            return False
    def discretize_line(self, n_space_point: int = 1000):
        disX = abs(self.start.x - self.end.x)
        disY = abs(self.start.y - self.end.y) 
        puntosdentro = []
        for i in range(n_space_point):
            puntosdentro.append(Point(i*(disX/n_space_point),
                                      i*(disY/n_space_point)))
        return puntosdentro

class Rectangle:
    def __init__(self, width: float = 0, height: float = 0,
                botton_left: "Point" = None,
                center: "Point" = None,
                upper_right: "Point" = None,
                line_der: "Line" = None,
                line_izq: "Line" = None,
                line_sup: "Line" = None,
                line_inf: "Line" = None):
        self.width = width
        self.height = height
        self.botton_left = botton_left
        self.center = center
        self.upper_right = upper_right
        self.line_der = line_der
        self.line_izq = line_izq
        self.line_sup = line_sup
        self.line_inf = line_inf
    
        if botton_left != None and width != 0 and height != 0:
            self.center = Point(width/2 + self.botton_left.x,
                                 height/2 + self.botton_left.y)
            self.upper_right = Point(width + self.botton_left.x,
                                 height + self.botton_left.y)
        elif center != None and width != 0 and height != 0:
            self.botton_left = Point(self.center.x - width/2,
                                     self.center.y - height/2)
            self.upper_right = Point(self.center.x + width/2,
                                     self.center.y + height/2)
        elif botton_left != None and upper_right != None:
            self.width = self.upper_right.x - self.botton_left.x
            self.height = self.upper_right.y - self.botton_left.y
            self.center = Point(self.botton_left.x + self.width/2,
                                 self.botton_left.y + self.height/2)
        elif line_der != None and line_izq != None and line_sup != None and line_inf != None:
            self.botton_left = Point(self.line_izq.start.x,
                                     self.line_inf.start.y)
            self.upper_right = Point(self.line_der.end.x,
                                     self.line_sup.end.y)
            self.width = self.upper_right.x - self.botton_left.x
            self.height = self.upper_right.y - self.botton_left.y
            self.center = Point(self.botton_left.x + self.width/2,
                                 self.botton_left.y + self.height/2)
        else:
            print("Method no valido")

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2*self.width + 2*self.height
    
    def compute_interference_point(self, Point):
        punto = Point
        enX = False
        enY = False
        if self.botton_left.x <= punto.x <= self.upper_right.x:
            enX = True
        if self.botton_left.y <= punto.y <= self.upper_right.y:
            enY = True
        if enX and enY:
            return True
        else:
            return False
    
    def compute_interference_line(self, Line):
        linea = Line
        puntos = 1000
        disX = abs(linea.start.x - linea.end.x)
        disY = abs(linea.start.y - linea.end.y) 
        puntosdentro = []
        for i in range(puntos):
            if self.compute_interference_point(
                Point(i*(disX/puntos),i*(disY/puntos))):
                puntosdentro.append(Point(i*(disX/puntos),i*(disY/puntos)))
        return(puntosdentro[0].x,puntosdentro[0].y
               ,puntosdentro[-1].x,puntosdentro[-1].y)

class Square(Rectangle):
    def __init__(self, width: float = 0, height: float = 0,
                botton_left: "Point" = None,
                center: "Point" = None,
                upper_right: "Point" = None):
        self.height = height
        self.width = width
        height = width
        super().__init__(width, height, botton_left, center, upper_right)

punto1 = Point(2, 6)
linea1 = Line(start = Point(0,0), end = Point(5,5))
rectangulo1 = Rectangle(width = 5, height = 10, botton_left = Point(0, 0))
rectangulo2 = Rectangle(width = 5, height = 10, center =  Point(0, 0))
rectangulo3 = Rectangle(botton_left = Point(0, 0), upper_right= Point(5, 10))
rectangulo4 = Rectangle(line_der = Line(start = Point(5, 0), end = Point(5, 10)),
                       line_izq = Line(start = Point(0, 0), end = Point(0, 10)),
                       line_sup = Line(start = Point(0, 10), end = Point(5, 10)),
                       line_inf = Line(start = Point(0, 0), end = Point(0, 5)))
cuadrado1 = Square(width = 5, botton_left = Point(0, 0))