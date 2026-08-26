from src.projeto.projeto_service import ProjetoService
from src.usuario.usuario_service import UsuarioService

usuario_service = UsuarioService()
projeto_service = ProjetoService(usuario_service)

usuario1 = usuario_service.criar_usuario(nome="Vitor", email="vitor@gmail.com", senha=123456)
usuario2 = usuario_service.criar_usuario(nome="Ana", email= "ana@gmail.com", senha=123456)

usuario_service.listar_usuario()

projeto1 = projeto_service.criar_projeto(nome="POO", descricao="Teste", usuario_id=1)

projeto_service.listar_projetos()