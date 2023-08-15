
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def calculate_area(self):
        return self.height * self.width

    def get_string_depiction(self):
        for i in range(self.width):
            print("*", end=" ")

        print()

        for i in range(self.height - 2):
            print("*".ljust(self.width), end="")
            print("*".rjust(self.width - 1))

        for i in range(self.width):
            print("*", end=" ")

        print()
