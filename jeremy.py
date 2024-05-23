import pyxel
import math
from random import randint

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
        self.pocession_piece = False
        self.detec = Detection()
        self.move = Mouvements(self.x,self.y,self.saut)
        self.objet = Objets()
        pyxel.load("4.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)


    def update(self):
        self.x, self.o, self.saut, self.y = self.move.bouger(self.x, self.y, self.saut)
        self.t =(self.t +  8) % 40

        if not self.detec.bas(self.x, self.y) and not self.saut: 
            self.y += 1
            self.y = round(self.y, 0)

        
        self.pocession_redkey = self.detec.recuperer_redkey(self.pocession_redkey, self.x, self.y)
        self.pocession_greenkey = self.detec.recuperer_greenkey(self.pocession_greenkey, self.x, self.y)
        self.pocession_piece = self.detec.recuperer_piece(self.pocession_piece, self.x, self.y)


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

        if not self.pocession_piece:
            self.objet.piece(self.x)


class Objets():
    def __init__(self):
        pass

    def cle_rouge(self, x):
        pyxel.blt(41*8-x+60, 10*8, 0, 32, 192, 8, 8)
    
    def bloc_rouge(self, x):
        pyxel.blt(32*8-x+60, 5*8, 0, 32, 184, 8, 8)

    def cle_verte(self, x):
        pyxel.blt(30*8-x+60, 10*8, 0, 40, 192, 8, 8)
    
    def bloc_vert(self, x):
        pyxel.blt(36*8-x+60, 8*8, 0, 48, 184, 8, 8)
    
    def piece(self, x):
        if randint(0,1) == 1:
            pyxel.blt(41*8-x+60, 7*8, 0, 32, 160, 8, 8, 5)
        else:
            pyxel.blt(41*8-x+60, 7*8, 0, 48, 160, 8, 8, 5)
    

class Mouvements():
    def __init__(self, x, y, saut):
        self.o = 16
        self.sautencours = saut
        self.detec = Detection()
        self.y_init = 0
        self.angle = 0

    def bouger(self, x, y, saut):
        self.x = x
        self.y = y
        self.sautencours = saut

        if pyxel.btn(pyxel.KEY_Q) and not self.detec.gauche(self.x, self.y):
            self.x -= 1
            self.o = 24

        if pyxel.btn(pyxel.KEY_D) and not self.detec.droit(self.x, self.y):
            self.x += 1
            self.o = 16

        if pyxel.btn(pyxel.KEY_SPACE) and self.detec.bas(self.x, self.y):
            self.sautencours = True
            self.y_init = self.y

        if self.sautencours:
            self.saut()
            
            

        return self.x, self.o, self.sautencours, self.y

    def saut(self):
        self.angle += 10
        loop = math.radians(self.angle)
        self.y = self.y_init - math.sin(loop)*15
        if self.angle >= 120:
            print("A")
            self.sautencours = False
            self.angle = 0
        """if self.detec.bas(self.x, self.y):
            print("B")
            self.sautencours = False
            self.angle = 0"""
        

class Detection() :
    def __init__(self) :
        pass

    def bas (self, x, y):
        if x < 60:
            if pyxel.pget(x, y + 8) == 0 or pyxel.pget(x + 8, y + 8) == 0 or pyxel.pget(x + 4, y + 8) == 0:
                return True
        else:
            if pyxel.pget(60 ,y + 8) == 0 or  pyxel.pget(68, y + 8) == 0 or pyxel.pget(64, y + 8) == 0:
                return True
        return False
    
    def droit(self, x, y):
        if x < 60:
            if pyxel.pget(x+8,y) == 0 or  pyxel.pget(x+8,y+7) == 0:
                return True
        else:
            if pyxel.pget(68 ,y) == 0 or  pyxel.pget(68,y+7) == 0:
                return True

    def gauche(self, x, y):
        if x < 60:
            if pyxel.pget(x-1,y) == 0 or  pyxel.pget(x-1,y+7) == 0:
                return True
        else:
            if pyxel.pget(59 ,y) == 0 or  pyxel.pget(59,y+7) == 0:
                return True
    
    def recuperer_redkey(self, pocession_actuelle, x, y):
        if 388-x <= 68 and 388-x >= 52:
            if 64 <= y and y <= 80:
                return True
        return pocession_actuelle

    def recuperer_greenkey(self, pocession_actuelle, x, y):
        if 300-x <= 68 and 300-x >= 52:
            if 64 <= y and y <= 80:
                return True
        return pocession_actuelle

    def recuperer_piece(self, pocession_actuelle, x, y):
        if 388-x <= 68 and 388-x >= 52:
            if 52 <= y and y <= 64:
                return True
        return pocession_actuelle

App()


