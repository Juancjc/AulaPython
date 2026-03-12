"""
Arquivo: main.py
Descrição: Este arquivo é o ponto de entrada do programa.
"""

#declração de importação
from aluno import Aluno
from utilidades import verificar_aprovacao

def main():
    """
    Função principal do programa. que utiliza a classe Aluno para criar um objeto aluno e utilidades para verificar a aprovação do aluno com base na média de suas notas.
    """

    aluno1 = Aluno("João das Neves", 25, "12345", 8,9)
    print(aluno1.exibir_informacoes())
    mediaNota = aluno1.calcular_media()
    print(f"Média: {mediaNota}")
    print(verificar_aprovacao(mediaNota))

if __name__ == "__main__":
    main()