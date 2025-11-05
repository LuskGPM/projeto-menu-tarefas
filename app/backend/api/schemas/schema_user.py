from pydantic import BaseModel, Field, field_validator

class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=60)
    nickname: str = Field(min_length=3, max_length=90)
    senha_front: str = Field(min_length=8, description='Senha deve ter pelomenos 8 dígitos')
    
    @field_validator('nome')
    @classmethod
    def formatar_nome(cls, nome: str) -> str:
        return nome.strip().capitalize()
    
class UsuarioLogin(BaseModel):
    nickname: str = Field(min_length=3)
    senha_login: str = Field(min_length=8)
    
class UsuarioUpdate(BaseModel):
    nome: str | None = Field(None, min_length=3)
    nickname: str | None = Field(None, min_length=3)
    senha_antiga: str = Field(min_length=8)
    senha_nova: str | None = Field(None, min_length=8)
