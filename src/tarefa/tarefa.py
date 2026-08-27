#Declaração da classe Tarefa
from datetime import datetime


class Tarefa:

    #Variável para atualizar o ID automaticamente
    prox_id = 1

    #Declaração do Construtor
    def __init__(self, titulo, descricao, prioridade, data_limite, projeto):
        self.id = Tarefa.prox_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "EM ANDAMENTO"
        self.data_limite = data_limite
        self.projeto = projeto

    #Método para marcar a tarefa como concluída
    def marcar_concluida(self):
        self.status = "CONCLUIDA"

    #Método para validar se tarefa está vencida
    def esta_vencida(self):

        if self.status == "EM ANDAMENTO" or self.status == "PENDENTE":
            data_limite = datetime.strptime(self.data_limite, "%d/%m/%Y")
            data_atual = datetime.now()

            if data_limite < data_atual:
                self.status = "ATRASADO"
                print("A tarefa está atrasada e seu status foi alterado!")
                return True
            else:
                print("A tarefa está dentro do prazo!")
                return False

        else:
            print("A tarefa já está concluída!")
            return False