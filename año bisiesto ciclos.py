def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calcular_años_bisiestos(year):
    count=0
    for y in range(1900, year + 1):
        if es_bisiesto(y):
            count += 1
    return count 

entrada = int(input("Ingrese un año entre 1900 y 2199: "))

if 1900 <= entrada <= 2199:
    años_bisiestos = calcular_años_bisiestos(entrada)
    print(f"El numero de años bisiestos entre 1900 y {entrada} es: {años_bisiestos}")

else:
    print("El año ingresado esta fuera del rango permitido")