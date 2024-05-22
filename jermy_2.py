import pyxel
import math

class App:
    def __init__(self):
        pyxel.init(120, 120, title="Nuit du Code")
        self.x = 0
        self.y = 56
        self.t = 0
        self.angle = 0 
        self.saut = False
        self.pocession_redkey = False
        self.pocession_greenkey = False
        self.detec = Detection(self.x,self.y)
        self.move = Mouvements(self.x,self.y,self.saut)
        self.objet = Objets(self.x)
        pyxel.load("4.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)


    def update(self):
        self.x, self.o, self.saut, y_init = self.move.bouger(self.x,self.y, self.saut)
        self.t =(self.t +  8) % 40

        if not self.detec.bas(self.x,self.y) and not self.saut: 
            self.y += 1
        if self.saut:
            self.angle += 3
            loop = math.radians(self.angle)
            self.y = y_init - math.sin(loop)*2.2
            if self.angle >= 177:
                self.saut = False
                self.angle = 0
            if self.detec.bas(self.x,self.y): 
                self.saut = False
                self.angle = 0
        
        self.pocession_redkey = Detection(self.x, self.y).recuperer_redkey(self.pocession_redkey)
        self.pocession_greenkey = Detection(self.x, self.y).recuperer_greenkey(self.pocession_greenkey)


    def draw(self):

        pyxel.cls(0)
        if self.x >= 60:
            pyxel.bltm(0,0,0,self.x - 60,0,128,128)
            pyxel.blt(60,self.y,0,self.t,self.o,8,8, 5)
        else:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.blt(self.x,self.y,0,self.t,self.o,8,8,5)



        if not self.pocession_redkey:
            self.objet.cle_rouge(self.x)
        else:
            self.objet.bloc_rouge(self.x)

        if not self.pocession_greenkey:
            self.objet.cle_verte(self.x)
        else:
            self.objet.bloc_vert(self.x)


class Objets():
    def __init__(self, x):
        self.x = x

    def cle_rouge(self, x):
        pyxel.blt(41*8-x+60, 10*8, 0, 32, 192, 8, 8)
    
    def bloc_rouge(self, x):
        pyxel.blt(32*8-x+60, 5*8, 0, 32, 184, 8, 8)

    def cle_verte(self, x):
        pyxel.blt(30*8-x+60, 10*8, 0, 40, 192, 8, 8)
    
    def bloc_vert(self, x):
        pyxel.blt(36*8-x+60, 8*8, 0, 48, 184, 8, 8)
    
    def piece(self, x):
        pyxel.blt(30*8-x+60, 10*8, 0, 40, 192, 8, 8)
    
    



class Mouvements():
    def __init__(self, x,y,saut):
        self.x = x
        self.o = 16
        self.y = y
        self.saut = saut
        self.detec = Detection(self.x, self.y)
    def bouger(self,x,y,saut):
        self.x = x
        self.y = y
        self.saut = saut
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.o = 24
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
            self.o = 16
        if pyxel.btn(pyxel.KEY_SPACE): #and self.detec.bas(self.x,self.y):
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
            if pyxel.pget(self.x,self.y+8) == 0 or  pyxel.pget(self.x+8,self.y+8) == 0 or pyxel.pget(self.x+4,self.y+8) == 0:
                return True
        else:
            if pyxel.pget(60 ,self.y+8) == 0 or  pyxel.pget(68,self.y+8) == 0 or pyxel.pget(64,self.y+8) == 0:
                return True
        return False
    
    def recuperer_redkey(self, pocession_actuelle):
        if 41*8-self.x+60 <= 68 and 41*8-self.x+60 >= 52:
            return True
        return pocession_actuelle

    def recuperer_greenkey(self, pocession_actuelle):
        if 30*8-self.x+60 <= 68 and 30*8-self.x+60 >= 52:
            return True
        return pocession_actuelle

App()


