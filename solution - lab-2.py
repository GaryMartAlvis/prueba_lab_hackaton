def precios(edad: int):
    # Cambiar el valor de esta variable como corresponde
    if edad < 4:
        precio = 0
    if 4 <= edad < 19:
        precio = 5
    if edad >= 19:
        precio = 10

    return precio



def triangulo(n: int):
    res = ""

    # Concatenar cada linea a la variable `res`
    for i in range(1, n + 1):
        res += '*' * i
        if i < n:
            res += '\n'
    return res




