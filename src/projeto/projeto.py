#Import da biblioteca datetime
from datetime import datetime

#Declaração da classe Projeto
class Projeto:

    #Variável para atualizar automaticamente o id
    prox_id = 1

    #Declaração do construtor
    def __init__(self, nome, descricao, usuario):
        self.id = Projeto.prox_id
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = datetime.now()
        self.usuario = usuario

        Projeto.prox_id += 1