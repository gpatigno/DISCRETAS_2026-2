def euclides_extendido(a, b):
    """
    Algoritmo de Euclides Extendido (versión recursiva).

    Retorna:
        d = gcd(a, b)
        x, y = coeficientes de Bézout

    Cumple:
        a*x + b*y = d
    """

    # Caso base
    if b == 0:
        return a, 1, 0

    # Llamada recursiva
    d, x1, y1 = euclides_extendido(b, a % b)

    # Actualización de los coeficientes
    x = y1
    y = x1 - (a // b) * y1

    return d, x, y


# Ejemplo presentado en clase:
a = 240
b = 46

d, x, y = euclides_extendido(a, b)

print("  ")
print("a =", a)
print("b =", b)
print("gcd(a,b) =", d)
print("  ")
print("Coeficientes de Bézout encontrados:")
print("x =", x)
print("y =", y)
print("  ")
print("Verificación del cálculo con estos coeficientes de Bézout: a * x + b * y =", a * x + b * y)
print("  ")