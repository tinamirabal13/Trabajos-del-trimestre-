class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

class Barco(Vehiculo):
    def __init__(self, marca, modelo, longitud):
        super().__init__(marca, modelo)
        self.longitud = longitud

class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad

carro1 = Carro("Toyota", "Corolla", "Rojo")
carro2 = Carro("Honda", "Civic", "Azul")

barco1 = Barco("Yamaha", "1234", 30)
barco2 = Barco("Mercury", "5678", 40)

avion1 = Avion("Boeing", "747", 300)
avion2 = Avion("Airbus", "A380", 500)

print("Detalles del Carro 1:")
print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)
print("Color:", carro1.color)

print("\nDetalles del Carro 2:")
print("Marca:", carro2.marca)
print("Modelo:", carro2.modelo)
print("Color:", carro2.color)

print("\nDetalles del Barco 1:")
print("Marca:", barco1.marca)
print("Modelo:", barco1.modelo)
print("Longitud:", barco1.longitud)

print("\nDetalles del Barco 2:")
print("Marca:", barco2.marca)
print("Modelo:", barco2.modelo)
print("Longitud:", barco2.longitud)

print("\nDetalles del Avion 1:")
print("Marca:", avion1.marca)
print("Modelo:", avion1.modelo)
print("Capacidad:", avion1.capacidad)

print("\nDetalles del Avion 2:")
print("Marca:", avion2.marca)
print("Modelo:", avion2.modelo)
print("Capacidad:", avion2.capacidad)
