"""
Arquivo: aluno.py
Objeto: Aluno
Descrição: Este arquivo define a classe Aluno, que representa um aluno com atributos como nome, idade e matrícula.
 A classe inclui métodos para exibir as informações do aluno e calcular a média de suas notas.
"""
class Aluno:
    """
    Classe que representa um aluno.
    """
    def __init__(self, nome, idade, matricula, nota1=0, nota2=0):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def exibir_informacoes(self):
        """
        Método para exibir as informações do aluno.
        """
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")

    def calcular_media(self):
        """
        Calcula a media das notas do aluno.
        """
        media = (self.nota1+ self.nota2)/2
        return media