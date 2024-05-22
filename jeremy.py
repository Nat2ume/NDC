import pyxel
class App:
    def __init__(self):
        pyxel.init(120, 120, title="Nuit du Code")
        self.x = 0
        self.y = 40
        self.t = 0
        self.orientation = 16
        pyxel.load("4.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x, self.y, self.orientation = Mouvements(self.x, self.y).bouger()
        self.t =(self.t +  8) % 40
    def draw(self):

        pyxel.cls(0)
        if self.x >= 60:
            pyxel.bltm(0,0,0,self.x - 60,0,128,128)
            pyxel.blt(60,40,0,self.t,self.orientation,8,8)
        else:
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.blt(self.x,40,0,self.t,self.orientation,8,8)
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.orientation = 16

    def bouger(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.orientation = 24
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
            self.orientation = 16
        return self.x, self.y, self.orientation

App()
