This is a Trial Library Class to Calculate Volume of a Box:

Used code is :


---------In  classes.py-------
class Box:
    def __init__(self,length, width, height):
        self.length=length
        self.width=width
        self.height=height

    def getVolume(self):
        volume= self.length*self.width*self.height
        return volume

------------------------------


---------In  classes.py-------

from classes import Box

mybox= Box(10,3,10)
vol= mybox.getVolume()
print(vol)

------------------------------