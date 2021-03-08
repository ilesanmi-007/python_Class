class Triangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def area(self):
        self.width = float(input('enter the base value of your triangle: '))
        self.height = float(input('enter the height of your triangle: '))
        return (1/2*self.width * self.height)