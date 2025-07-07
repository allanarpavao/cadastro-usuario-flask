from pydantic import BaseModel
from typing import Optional, List

from datetime import datetime
from models.usuario import Usuario

class CadastroUsuarioSchema(BaseModel):
    """Especifica os atributos necessários para cadastrar um novo usuário
    """
    email: str = "exemplo@gmail.com"
    nome_usuario: str = "exemplo_usuario"
    senha: str = "senha123"

class UsuarioBuscaSchema(BaseModel):
    """ Modelo utilizado para consultas de usuário, utilizando apenas o nome de usuário como critério.
    """
    nome: str = "exemplo"

class ListagemUsuariosSchema(BaseModel):
    """ Representa o retorno de uma consulta que envolve vários usuários
    """
    usuarios:List[CadastroUsuarioSchema]

def apresenta_usuario(usuario:Usuario):
    """ Gera um dicionário com os dados do usuário conforme o UsuarioViewSchema.
    """
    return {
            "email": usuario.email,
            "nome_usuario": usuario.nome_usuario,
            "data_insercao": usuario.data_insercao
        }

def apresenta_usuarios(usuarios:List[Usuario]):
    """ Cria uma representação padronizada para múltiplos usuários
    """
    result = []
    for usuario in usuarios:
        result.append({
            "email": usuario.email,
            "nome_usuario": usuario.nome_usuario,
            "data_insercao": usuario.data_insercao
        })

    return {"usuarios": result}

class UsuarioViewSchema(BaseModel):
    """ Especifica o formato dos dados apresentados ao exibir um usuário
    """
    email: str
    nome_usuario: str
    data_insercao: datetime