

# Area de un poligono

poligonos = ["Triángulo", "Cuadrado", "Rectángulo"]

print("Menu")
for n, p in enumerate(poligonos, start=1):
    print(f"{n}: {p}")
print("")

int_poligono = int(input("Seleccione el numero del poligono"))

#Triangulo
if (int_poligono == 1):

    base = int(input("escribir la base en cm: "))
    altura= int(input("escribir la altura en cm: "))

    resultado = (base * altura) / 2

    print(f"el area del triangulo es: ¨{resultado} cm2")


#Cuadrado
elif (int_poligono == 2):
    lado = int(input("colocar el lado del cuadrado en cm: "))

    resultado = (lado * lado)

    print(f"El area del cuadrado es: {resultado} cm2")

#Rectangulo
elif (int_poligono == 3):

    lado = int(input("colocar la altura rectangulo en cm: "))

    base = int(input("colocar la base del rectangulo en cm: "))

    resultado = (base * lado)
    print(f"el area del rectangulo es: {resultado} cm2")

else:

    print("no existe")
