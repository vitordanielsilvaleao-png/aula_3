#Import da classe Projeto do arquivo projeto.py
from src.projeto.projeto import Projeto

#Declaração da classe ProjetoService
class ProjetoService:

    #Declaração do Construtor
    def __init__(self, usuario_service):
        self.lista_projetos =[]
        self.usuario_service = usuario_service

    #Método para adicionar projeto
    def criar_projeto(self, nome, descricao, usuario_id):
        usuario = self.usuario_service.buscar_usuario(usuario_id)
        registro_projeto = Projeto(nome, descricao, usuario)
        self.lista_projetos.append(registro_projeto)

        return registro_projeto

    #Método para listar projeto
    def listar_projetos(self):

        print("*******************************")
        print("\n\t PROJETOS CADASTRADOS\n")

        for registro_projeto in self.lista_projetos:
            print("ID: ", registro_projeto.id)
            print("Nome: ", registro_projeto.nome)
            print("Descrição: ", registro_projeto.descricao)
            print("Data de Criação: ", registro_projeto.data_criacao)
            print("ID do Usuário: ", registro_projeto.usuario.id)
            print("Nome do Usuário: ", registro_projeto.usuario.nome)
            print("E-mail do Usuário: ", registro_projeto.usuario.email)
            print("*******************************\n")

    #Método para remover projeto
    def remover_projeto(self, id):

        for registro_projeto in self.lista_projetos:

            if id == registro_projeto.id:
                self.lista_projetos.remove(registro_projeto)
                print("Removendo projeto ....... \nProjeto removido com sucesso!\n")
                return

        print("O projeto especificado não está cadastrado!\n")