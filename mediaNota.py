nome = input("Digite seu nome: ")
#(n1+trab01)+(n2+trb02)/2=media
#media > 7 = Aprovado
#media estiver entre 4 e 7 = Final
#media < 4 = Reprovado
provaN1 = float(input("Digite sua nota da N1: "))
trabalho1 = float(input("Digite sua nota do trabalho 1: "))
provaN2 = float(input("Digite sua nota da N2: "))
trabalho2 = float(input("Digite sua nota do trabalho 2: "))

media = ((provaN1 + trabalho1) + (provaN2 + trabalho2)) / 2
resultado = ""
if media > 7:
    resultado = "Aprovado"
elif media >= 4 and media <= 7:
    resultado = "Final"
else:
    resultado = "Reprovado"
#case
provaIFinal = 0
match resultado:
    case "Aprovado":
        print(f"{nome} você foi {resultado} com a média {media:.2f}")
    case "Final":
        print(f"{nome} você está de {resultado} com a média {media:.2f} você precisa fazer a prova final")
        print("Digite a nota da prova final")
        provaIFinal = float(input())
    case "Reprovado":
        print(f"{nome} você foi {resultado} com a média {media:.2f} agora vai ter que fazer no próximo período")
    case _:
        print("Resultado desconhecido")

#media da final
#a soma da media com a prova final tem que ser supeiror a 10
resultadoFinal = media + provaIFinal

if resultadoFinal >= 10:
    print(f"{nome} você foi aprovado na prova final com a média final de {resultadoFinal:.2f}")
else:
    print('Até o próximo período, estude mais e tente novamente')