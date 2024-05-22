import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        pyxel.load("4.pyxres")
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)
    def update(self):
        self.x, self.y = Mouvements(self.x, self.y).bouger()
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        pyxel.blt(self.x, self.y, 0, 0, 16, 8, 8)

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
    

App()