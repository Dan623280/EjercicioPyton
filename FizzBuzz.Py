
def numero_primo3(numero):

    valor = numero / 3

    if valor.is_integer():

        return True

    return False

def numero_primo5(numero):

    valor = numero / 5

    if valor.is_integer():

        return True

    return False



for i in range(100):

    print(" ")
    print(i)
    if numero_primo3(i) and numero_primo5(i):
        
        print("Fizz Buzz")

    elif numero_primo3(i):
        
        print("Fizz")

    elif numero_primo5(i):
        
        print("Buzz")

    