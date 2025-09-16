#Jogo de adivinhação

import random 
secreto = random.randint(1, 10)
chute = 0
while chute != secreto:
    chute = int(input('Adivinha o número entre 1 e 10: '))
    if chute < secreto:
        print ('Tente um número maior!')
    elif chute > secreto:
        print('Tente um número menor!')
else:
    print('Parabéns! Você acertou.')