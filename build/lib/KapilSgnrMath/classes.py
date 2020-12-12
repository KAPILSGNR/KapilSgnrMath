class Box:
    def __init__(self,length, width, height):
        self.length=length
        self.width=width
        self.height=height

    def getVolume(self):
        volume= self.length*self.width*self.height
        return volume


print("Wow! It's Working")
print("Volume of the Box is from classes.py file")
