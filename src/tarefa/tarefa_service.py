#Import da classe Tarefa do arquivo tarefa.py
from src.tarefa.tarefa import Tarefa

#Declaração da classe TarefaService
class TarefaService:

    #Declaração do construtor
    def __init__(self, projeto_service):
        self.lista_tarefas = []
        self.projeto_service = projeto_service

    #Método para adicionar tarefa
    def criar_tarefa(self, titulo, descricao, prioridade, data_limite, projeto_id):
        projeto = self.projeto_service.buscar_projeto(projeto_id)
        registro_tarefa = Tarefa(titulo, descricao, prioridade, data_limite, projeto)
        self.lista_tarefas.append(registro_tarefa)

        return registro_tarefa

    #Método para listar tarefas
    def listar_tarefas(self):

        print("*******************************")
        print("\n\t TAREFAS CADASTRADAS\n")

        for registro_tarefa in self.lista_tarefas:
            print("ID: ", registro_tarefa.id)
            print("Título: ", registro_tarefa.titulo)
            print("Descrição: ", registro_tarefa.descricao)
            print("Data Limite: ", registro_tarefa.data_limite)
            print("Prioridade: ", registro_tarefa.prioridade)
            print("Status: ", registro_tarefa.status)
            print("ID do Projeto Associado: ", registro_tarefa.projeto.id)
            print("Nome do Projeto Associado: ", registro_tarefa.projeto.nome)
            print("Data de Criação do Projeto Associado: ", registro_tarefa.projeto.data_criacao)
            print("*******************************\n")

    #Método para remover tarefa
    def remover_tarefa(self, id):

        for registro_tarefa in self.lista_tarefas:

            if id == registro_tarefa.id:
                self.lista_tarefas.remove(registro_tarefa)
                print("Removendo tarefa ....... \nTarefa removida com sucesso!\n")
                return

        print("A tarefa especificada não está cadastrada!\n")

    #Método para buscar tarefa pelo ID
    def buscar_tarefa(self, id):

        for registro_tarefa in self.lista_tarefas:

            if id == registro_tarefa.id:
                return registro_tarefa

        print("A tarefa especificada não está cadastrada!\n")
