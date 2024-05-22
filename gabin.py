import pyxel
import math
class App:
    def __init__(self):
        pyxel.init(120, 120, title="Nuit du Code")
        self.x = 0
        self.y = 56
        self.t = 0
        self.angle = 0 
        self.o = 16
        self.saut = False
        self.detec = Detection(self.x,self.y)
        self.move = Mouvements(self.x,self.y,self.saut)
        pyxel.load("4.pyxres")
        pyxel.run(self.update, self.draw)
         
    def bas (self):
        if self.x < 60:
            if pyxel.pget(self.x,self.y+8) == 0 or  pyxel.pget(self.x+8,self.y+8) == 0:
                return True
        else:
            if pyxel.pget(60 ,self.y+8) == 0 or  pyxel.pget(68,self.y+8) == 0:
                return True
        return False
    
    def bouger(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.o = 24
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
            self.o = 16
        if pyxel.btn(pyxel.KEY_SPACE) and self.bas():
            self.y -= 5
            self.saut = True
        return self.x,self.o, self.saut, self.y

    def update(self):
        self.x, self.o, self.saut, y_init = self.bouger()
        self.t =(self.t +  8) % 40

        if not self.detec.bas(self.x,self.y) and not self.saut: 
            self.y += 1
        print(self.saut,self.bas())
        if self.saut:
            self.angle += 3
            loop = math.radians(self.angle)
            self.y = y_init - math.sin(loop)*2
            print(self.angle)
            if self.angle >= 180:
                self.saut = False
                self.angle = 0
            if self.bas(): 
                self.saut = False
                self.angle = 0
    def draw(self):

        pyxel.cls(0)
        if self.x >= 60:
            pyxel.bltm(0,0,0,self.x - 60,0,128,128)
            pyxel.blt(60,self.y,0,self.t,self.o,8,8, 5)
        else:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.blt(self.x,self.y,0,self.t,self.o,8,8,5)
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
    def __init__(self, x,y,saut):
        self.x = x
        self.o = 16
        self.y = y
        self.saut = saut
        #self.detec = Detection()
    def bouger(self,x,y):
        self.x = x
        self.y = y
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.o = 24
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
            self.o = 16
        if pyxel.btn(pyxel.KEY_SPACE) and Detection(self.x, self.y).bas(self.x,self.y):
            self.saut = True
        return self.x,self.o, self.saut, self.y

class Detection() :
    def __init__(self,x,y) :
        self.x = x 
        self.y = y
    def bas (self,x,y):
        self.x = x 
        self.y = y
        if self.x < 60:
            if pyxel.pget(self.x,self.y+8) == 0 or  pyxel.pget(self.x+8,self.y+8) == 0:
                return True
        else:
            if pyxel.pget(60 ,self.y+8) == 0 or  pyxel.pget(68,self.y+8) == 0:
                return True
        return False
App()


