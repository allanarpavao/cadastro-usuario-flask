from datetime import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, DateTime, Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from models import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    nome_usuario: Mapped[str] = mapped_column(String(30), unique=True, primary_key=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(30), nullable=False)
    data_insercao: Mapped[Optional[datetime]] = mapped_column(DateTime(), default=datetime.now())

    def __init__(self, email:str, nome_usuario:str, senha:str, data_insercao:Optional[DateTime] = None):
        self.email = email
        self.nome_usuario = nome_usuario
        self.senha = senha

        if data_insercao:
            self.data_insercao = data_insercao

    def __repr__(self) -> str:
        return f"Usuário(nome_usuario={self.nome_usuario!r}, email={self.email!r})"