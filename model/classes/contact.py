from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator


class Contact(BaseModel):
    id: Optional[int] = None
    title: str
    name: str
    company_name: Optional[str] = None
    email: EmailStr
    phone_number: str
    body: str
    delete_flg: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @field_validator("title")
    def validate_title(cls, title):
        if not title:
            raise ValueError("'title' must not be None.")
        if len(title) > 50:
            raise ValueError("'title' are limited to 50 characters.")
        return title

    @field_validator("name")
    def validate_name(cls, name):
        if not name:
            raise ValueError("'name' must not be None.")
        if len(name) > 60:
            raise ValueError("'name' are limited to 60 characters.")
        return name

    @field_validator("company_name")
    def validate_company_name(cls, company_name):
        if len(company_name) > 140:
            raise ValueError("'company_name' are limited to 140 characters.")
        return company_name

    @field_validator("email")
    def validate_email(cls, email):
        if not email:
            raise ValueError("'email' must not be None.")
        return email

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number):
        if not phone_number:
            raise ValueError("'phone_number' must not be None.")
        if len(phone_number) > 25:
            raise ValueError("'phone_number' are limited to 60 characters.")
        return phone_number

    @field_validator("body")
    def validate_body(cls, body):
        if not body:
            raise ValueError("'body' must not be None.")
        return body

    class Config:
        from_attributes = True
