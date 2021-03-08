class Triangle:
    def __init__(self, base = 0, height = 0):
        self.base = base
        self.height = height

    def area(self):
        #decided to try the inputing
        self.base = float(input('enter the base value of your triangle: '))
        self.height = float(input('enter the height of your triangle: '))
        return (0.5*self.base * self.height)