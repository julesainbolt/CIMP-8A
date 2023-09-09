
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def calculate_area(self):
        return self.height * self.width

    def __str__(self):
        return ("* " * self.width) + "\n" + \
         ("*".ljust(self.width) + "*\n".rjust(self.width)) * (self.height - 2) + \
         ("* " * self.width)


class Square(Rectangle):
    def __init__(self, length):
        Rectangle.__init__(self, height=length, width=length)
        self.length = length

    def calculate_perimeter(self):
        return self.length * 4

    def calculate_area(self):
        return self.length ** 2

    def __str__(self):
        return ("* " * self.width) + "\n" + \
         ("*".ljust(self.width) + "*\n".rjust(self.width)) * (self.height - 2) + \
         ("* " * self.width)
