import pyxel
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
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)
