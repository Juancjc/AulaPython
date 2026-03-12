"""
Arquivo: utilidades.py
Descrição: Este arquivo define funções utilitárias que podem ser usadas em diferentes partes do projeto.
"""

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"