import pyxel
class App:
    def __init__(self,move):
        pyxel.init(120, 120, title="Nuit du Code")
        self.x = 0
        self.bouge = move
        self.t = 0
        pyxel.load("4.pyxres")
        pyxel.run(self.update, self.draw)
    def update(self):
        self.x = ( self.bouge.bouger()[0]) % pyxel.width
        self.t =(self.t +  8) % 40
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,self.x*2,16,128,128)
        pyxel.blt(self.x,40,0,self.t,16,8,8)



class Mouvements():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def bouger(self):
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
        return self.x, self.y

move = Mouvements(0,0)
App(move)


