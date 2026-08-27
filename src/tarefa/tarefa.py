#Declaração da classe Tarefa

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