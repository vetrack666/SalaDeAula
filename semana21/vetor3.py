numeros = []
for i in range (10):
    valor = int(input(f'Digite {i + 1}° numero: '))
    numeros.append (valor)
print ('\nVetor completo: ', numeros)
print ('numeros pares: ')
for n in numeros:
    if n % 2 == 0:
        print (n, end = '-')