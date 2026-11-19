
numero_1 = 0

numero_2 = 1

print(numero_1)
print(numero_2)

for i in range(48):

    numero_3 = numero_2
    numero_2 = numero_1 + numero_2
    numero_1 = numero_3

    print(i, ": ",  numero_2)