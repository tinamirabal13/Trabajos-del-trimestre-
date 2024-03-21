class Seller:
    def __init__(self, name):
        self.name = name

class Vehiculo:
    def __init__(self, marca, modelo, seller):
        self.marca = marca
        self.modelo = modelo
        self.seller = seller

class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, seller):
        super().__init__(marca, modelo, seller)
        self.color = color

class Barco(Vehiculo):
    def __init__(self, marca, modelo, longitud, seller):
        super().__init__(marca, modelo, seller)
        self.longitud = longitud

class Avion(Vehiculo):
    def __init__(self, marca, modelo, capacidad, seller):
        super().__init__(marca, modelo, seller)
        self.capacidad = capacidad

carro1_seller = Seller("Toyota Dealership")
carro2_seller = Seller("Honda Dealership")
barco1_seller = Seller("Yamaha Dealership")
barco2_seller = Seller("Mercury Dealership")
avion1_seller = Seller("Boeing Dealership")
avion2_seller = Seller("Airbus Dealership")

carro1 = Carro("Toyota", "Corolla", "Rojo", carro1_seller)
carro2 = Carro("Honda", "Civic", "Azul", carro2_seller)
barco1 = Barco("Yamaha", "1234", 30, barco1_seller)
barco2 = Barco("Mercury", "5678", 40, barco2_seller)
avion1 = Avion("Boeing", "747", 300, avion1_seller)
avion2 = Avion("Airbus", "A380", 500, avion2_seller)

carro1.seller = Seller("New Toyota Dealership")

print("Detalles del Carro 1:")
print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)
print("Color:", carro1.color)
print("Concesionario:", carro1.seller.name)

print("\nDetalles del Carro 2:")
print("Marca:", carro2.marca)
print("Modelo:", carro2.modelo)
print("Color:", carro2.color)
print("Concesionario:", carro2.seller.name)

print("\nDetalles del Barco 1:")
print("Marca:", barco1.marca)
print("Modelo:", barco1.modelo)
print("Longitud:", barco1.longitud)
print("Concesionario:", barco1.seller.name)

print("\nDetalles del Barco 2:")
print("Marca:", barco2.marca)
print("Modelo:", barco2.modelo)
print("Longitud:", barco2.longitud)
print("Concesionario:", barco2.seller.name)

print("\nDetalles del Avion 1:")
print("Marca:", avion1.marca)
print("Modelo:", avion1.modelo)
print("Capacidad:", avion1.capacidad)
print("Concesionario:", avion1.seller.name)

print("\nDetalles del Avion 2:")
print("Marca:", avion2.marca)
print("Modelo:", avion2.modelo)
print("Capacidad:", avion2.capacidad)
print("Concesionario:", avion2.seller.name)

