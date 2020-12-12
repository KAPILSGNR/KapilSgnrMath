class Rectangle:

    def __init__(self,length, width):
        self.length=length
        self.width=width


    def getArea(self):
        area= self.length*self.width
        print("Area of the Rectangle is: ", area)
        return area