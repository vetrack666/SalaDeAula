# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Verificar se a idade é suficiente para tirar a CNH
if idade >= 18:
    # Verificar se a idade está dentro da faixa permitida para a CNH
    if idade <= 75:
        print("Você tem idade suficiente para tirar a CNH.")
    else:
        print("Sua idade é muito avançada para tirar a CNH.")
else:
    print("Você ainda não tem idade suficiente para tirar a CNH.")
