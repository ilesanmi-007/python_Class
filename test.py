from Rectangle import Rectangle
from Triangle import Triangle
from Square import square

def main():
    rect = Rectangle()
    sq = square(6)
    tri = Triangle()
    rect.breadth = 5
    rect.length = 30

    sq.length= 6
    tri = Triangle()
    result1 = rect.area()
    result2 = tri.area()
    result3 = sq.area()
    #always observe the object used
    final = result3 + result2 + result1
    print("behold... the reuslt", final)


main()