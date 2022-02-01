class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (((self.width ** 2) + (self.height ** 2)) ** .5)
        return self.diagonal

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            n = ''
            for c in range(0, self.height):
                for l in range(0, self.width):
                    n += '*'
                n += '\n'      
            return n

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, sq):
        h = self.height // sq.height
        w = self.width // sq.width
        return h*w


 

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_diagonal(self):
        self.diagonal = (((self.width ** 2) + (self.height ** 2)) ** .5)
        return self.diagonal

    def set_side(self, side):
        self.width = side
        self.height = side

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            n = ''
            for c in range(0, self.height):
                for l in range(0, self.width):
                    n += '*'
                n += '\n'      
            return n

    def __str__(self):
        return f'Square(side={self.width})'


#rect = Rectangle(5, 10)
#print(rect.get_area())
#rect.set_width(3)
#print(rect.get_perimeter())
#print(rect)

#sq = Square(9)
#print(sq.get_area())
#sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)

#print(sq.get_picture())

#rect.set_height(8)
#rect.set_width(16)
#print(rect.get_amount_inside(sq))


