
listadiv =[2,3,5,7]
def numero_primo(n):


    verifi = True

    for i in listadiv:

        resultado = n/i

        if resultado.is_integer():

            verifi = False

    return verifi

numero_input = int(input("Colocar numero primo"))


if numero_primo(numero_input):

    print("")
    print("numero no es primo")
    print("")

else:
    print("")
    print("numero es primo")
    print("")



for numero in range(1,101):

    if  (numero_primo(numero) or  numero in listadiv) and not numero <=1 :

        print(numero)


