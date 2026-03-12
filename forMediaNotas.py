import statistics

def calcular_media_notas(notas):
    if not notas:
        return 0
    return statistics.mean(notas)

# ler 5 notas
#array tem index, ou seja,
#cada elemento tem um número associado a ele,
#começando do 0
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

print(calcular_media_notas(notas))

