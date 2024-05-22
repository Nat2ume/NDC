import pyxel
import math
class App:
    def __init__(self):
        pyxel.init(120, 120, title="Nuit du Code")
        self.x = 0
        self.y = 50 
        self.t = 0
        self.angle = 0 
        self.saut= False
        pyxel.load("4.pyxres")
        pyxel.run(self.update, self.draw)
    def update(self):
        self.x,self.o, self.saut = Mouvements(self.x, self.y,self.saut).bouger()
        self.t =(self.t +  8) % 40
        if self.saut is True :
            self.angle += 1
            loop = math.radians(self.angle)
            self.y = self.y - math.cos(loop)

    def draw(self):

        pyxel.cls(0)
        if self.x >= 60:
            pyxel.bltm(0,0,0,self.x - 60,0,128,128)
            pyxel.blt(60,self.y,0,self.t,self.o,8,8)
        else:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.blt(self.x,self.y,0,self.t,self.o,8,8)
        Objets(self.x).cle_rouge()
        Objets(self.x).cle_verte()


class Objets():
    def __init__(self, x):
        self.x = x

    def cle_rouge(self):
        pyxel.blt(41*8-self.x+60, 10*8, 0, 32, 192, 8, 8)

    def cle_verte(self):
        pyxel.blt(30*8-self.x+60, 10*8, 0, 40, 192, 8, 8)


class Mouvements():
    def __init__(self, x, y,saut):
        self.x = x
        #self.y = y
        self.o = 16
        self.saut = False
    def bouger(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.o = 24
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
            self.o = 16
        if pyxel.btn(pyxel.KEY_SPACE):
                self.saut = True
        return self.x,self.o, self.saut 

class Detection() :
    def __init__(self) :
        pass
App()


