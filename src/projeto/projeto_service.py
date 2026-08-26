from src.projeto.projeto import Projeto

class ProjetoService:

    def __init__(self, usuario_service):
        self.lista_projetos =[]
        self.usuario_service = usuario_service

    def criar_projeto(self, nome, descricao, usuario_id):
        usuario = self.usuario_service.buscar_usuario(usuario_id)
        registro_projeto = Projeto(nome, descricao, usuario)
        self.lista_projetos.append(registro_projeto)

        return registro_projeto

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