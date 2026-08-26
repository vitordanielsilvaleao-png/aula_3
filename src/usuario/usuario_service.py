from src.usuario.usuario import Usuario

class UsuarioService:

    def __init__(self):
        self.lista_usuarios = []

    def criar_usuario(self, nome, email, senha):
        registro_usuario = Usuario(nome,email, senha)
        self.lista_usuarios.append(registro_usuario)

        return registro_usuario

    def listar_usuario(self):

        print("*******************************")
        print("\n\t USUÁRIOS CADASTRADOS\n")

        for registro_usuario in self.lista_usuarios:
            print("ID: ", registro_usuario.id)
            print("Nome: ", registro_usuario.nome)
            print("E-mail: ", registro_usuario.email)
            print("*******************************\n")

    def remover_usuario(self, id):

        for registro_usuario in self.lista_usuarios:

            if id == registro_usuario.id:
                self.lista_usuarios.remove(registro_usuario)
                print("Removendo usuário ....... \nUsuário removido com sucesso!\n")
                return

        print("O colaborador especificado não está cadastrado!\n")

