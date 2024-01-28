def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calcular_años_bisiestos(year):
    if 1900 <= year <= 2199:
        count = (year - 1900) // 4 - (year - 1900) // 100 + (year - 1600) // 400
        return count 
    else:
        return -1
    
entrada = int(input("Ingrese un año entre 1900 y 2199: "))
años_bisiestos = calcular_años_bisiestos(entrada)
if años_bisiestos != -1:
    print(f"El numero de años bisiestos entre 1900 y {entrada} es: {años_bisiestos}")
else:
    print("El año ingresado esta fuera del rango permitido")