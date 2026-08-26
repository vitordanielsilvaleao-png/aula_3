from datetime import datetime

class Projeto:

    prox_id = 1

    def __init__(self, nome, descricao, usuario):
        self.id = Projeto.prox_id
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = datetime.now()
        self.usuario = usuario

        Projeto.prox_id += 1