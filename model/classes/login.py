from pydantic import BaseModel, EmailStr, SecretStr


class Login(BaseModel):
    email: EmailStr
    password: SecretStr

    class Config:
        from_attributes = True
