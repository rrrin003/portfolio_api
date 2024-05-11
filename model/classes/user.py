from typing import Optional

from pydantic import BaseModel, EmailStr, SecretStr, field_validator

from common.common import hash_password


class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    password: SecretStr
    salt: Optional[SecretStr] = None
    delete_flg: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @field_validator("name")
    def validate_name(cls, name):
        if not name:
            raise ValueError("'name' must not be None.")
        if len(name) > 60:
            raise ValueError("'name' are limited to 60 characters.")
        return name

    @field_validator("email")
    def validate_email(cls, email):
        if not email:
            raise ValueError("'email' must not be None.")
        return email

    @field_validator("password")
    def validate_password(cls, password):
        pass_seclet_value = password.get_secret_value()
        if not pass_seclet_value:
            raise ValueError("'password' must not be None.")
        if len(pass_seclet_value) < 8:
            raise ValueError("'password' must be at least 8 characters long.")
        elif len(pass_seclet_value) > 24:
            raise ValueError("'password' must be less than 24 characters.")
        return hash_password(pass_seclet_value)

    class Config:
        from_attributes = True
