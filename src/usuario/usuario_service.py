#Import da classe Usuário do arquivo usuario.py
from src.usuario.usuario import Usuario

#Declaração da classe UsuarioService
class UsuarioService:

    #Declaração do construtor
    def __init__(self):
        self.lista_usuarios = []

    #Método para adicionar usuário
    def criar_usuario(self, nome, email, senha):
        registro_usuario = Usuario(nome,email, senha)
        self.lista_usuarios.append(registro_usuario)

        return registro_usuario

    #Método para listar usuários
    def listar_usuario(self):

        print("*******************************")
        print("\n\t USUÁRIOS CADASTRADOS\n")

        for registro_usuario in self.lista_usuarios:
            print("ID: ", registro_usuario.id)
            print("Nome: ", registro_usuario.nome)
            print("E-mail: ", registro_usuario.email)
            print("*******************************\n")

    #Método para remover usuário
    def remover_usuario(self, id):

        for registro_usuario in self.lista_usuarios:

            if id == registro_usuario.id:
                self.lista_usuarios.remove(registro_usuario)
                print("Removendo usuário ....... \nUsuário removido com sucesso!\n")
                return

        print("O colaborador especificado não está cadastrado!\n")

    #Método para buscar usuário pelo ID
    def buscar_usuario(self, id):

        for registro_usuario in self.lista_usuarios:

            if id == registro_usuario.id:
                return registro_usuario

        print("O colaborador especificado não está cadastrado!\n")