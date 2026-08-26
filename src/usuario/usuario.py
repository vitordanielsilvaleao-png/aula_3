#Declaração da classe Usuario
class Usuario:

    #Variável para geração automática de ID's
    prox_id = 1

    #Construtor da classe Usuario
    def __init__(self, nome, email, senha):
        self.id = Usuario.prox_id
        self.nome = nome
        self.email = email
        self.senha = senha

        Usuario.prox_id += 1