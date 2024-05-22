import pyxel
class App:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        self.x = 0
        pyxel.run(self.update, self.draw)
    def fond(self):
        pass
        


App()