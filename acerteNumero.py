import random
#randomizando valores
print("Bem-vindo ao jogo de adivinhação!🕹🎮")

numero_secreto = random.randint(1, 10)
print(numero_secreto)
seu_numero =int(input("Digite seu número: "))

if seu_numero == numero_secreto:
    print("Parabéns vc acertou🙌")
elif seu_numero < numero_secreto:
    print("O número secreto é maior do que o seu número.")
elif seu_numero > numero_secreto:
    print("O número secreto é menor do que o seu número.")
else:
    print("Ops, algo deu errado. Tente novamente.")
