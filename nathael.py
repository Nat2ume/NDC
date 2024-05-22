import pyxel
import pyxel
import math
class App:
    def __init__(self):
        pyxel.load("4.pyxres")
        pyxel.playm(0, loop=True)
        n = Detection()

    def draw(self):

        pyxel.cls(0)
        if self.n.over() == True:
            pyxel.cls(0)
        if self.x >= 60:
            pyxel.bltm(0,0,0,self.x - 60,0,128,128)
            pyxel.blt(60,self.y,0,self.t,self.o,8,8, 5)
        else:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.blt(self.x,self.y,0,self.t,self.o,8,8,5)

class Detection() :
    def __init__(self,x,y) :
        self.x = x 
        self.y = y
    def bas (self):
        if self.x < 60:
            if pyxel.pget(self.x,self.y+8) == 0 or  pyxel.pget(self.x+8,self.y+8) == 0:
                return True
        else:
            if pyxel.pget(60 ,self.y+8) == 0 or  pyxel.pget(68,self.y+8) == 0:
                return True
    def over(self):
        if self.x < 60:
            if pyxel.pget(self.x,self.y+8) == 10 or  pyxel.pget(self.x+8,self.y+8) == 10 or pyxel.pget(self.x,self.y+8) == 11 or  pyxel.pget(self.x+8,self.y+8) == 11:
                return True
        else:
            if pyxel.pget(60 ,self.y+8) == 10 or  pyxel.pget(68,self.y+8) == 10 or pyxel.pget(60 ,self.y+8) == 11 or  pyxel.pget(68,self.y+8) == 11:
                return True