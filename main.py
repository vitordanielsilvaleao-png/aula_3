from src.usuario.usuario_service import UsuarioService

teste = UsuarioService()

usuario1 = teste.criar_usuario(nome="Vitor", email="vitor@gmail.com", senha=123456)
usuario2 = teste.criar_usuario(nome="Ana", email= "ana@gmail.com", senha=123456)

teste.listar_usuario()

teste.remover_usuario(2)

teste.listar_usuario()
