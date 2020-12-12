print("Wow! It's Working")
print("Volume of the Box is from classes.py file")


class Box:
    def __init__(self,length, width, height):
        self.length=length
        self.width=width
        self.height=height

    def getVolume(self):
        volume= self.length*self.width*self.height
        print("Volume of the Box is: ", volume)
        return volume

    def getArea(self):
        area= self.length*self.width
        print("Volume of the Box is: ", area)
        return area