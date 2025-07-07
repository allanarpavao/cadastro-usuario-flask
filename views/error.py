from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """Descreve a estrutura de resposta para situações de erro.
    """
    message: str