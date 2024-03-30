class Casa:
    def __init__(self, color) -> None:
        self.color = color
        self.consumo_de_luz = 0
        self.consumo_de_agua = 0
    
    def pintar(self, color):
        self.color = color

    def prender_luz(self):
        self.consumo_de_luz += 10

    def abrir_ducha(self):
        self.consumo_de_agua += 10
    
    def tocar_timbre(self):
        print("RRRRIIIIIIING")
        self.consumo_de_luz += 2

class Mansion(Casa):
    def prender_luz(self):
        self.consumo_de_luz += 50
    
    def abrir_ducha(self):
        self.consumo_de_agua += 50

    def tocar_timbre(self):
        print("DING DONG")
        self.consumo_de_luz += 3

miCasa = Casa("Rojo")
miCasa.pintar("Azul")
print(miCasa.color)

miCasa.tocar_timbre()
print(miCasa.consumo_de_luz)

miCasa.abrir_ducha()
print(miCasa.consumo_de_agua)

miMansion = Mansion("Blanco")
print(miMansion.color)

miMansion.tocar_timbre()
miMansion.pintar("Café")

print(miMansion.color)