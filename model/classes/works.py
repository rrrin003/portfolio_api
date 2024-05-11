import json
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Works(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=50)
    body: Optional[str] = Field(None, max_length=200)
    photo: Optional[dict] = None
    tag: Optional[dict] = None
    draft_flg: Optional[bool] = None
    hidden_flg: Optional[bool] = None
    delete_flg: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @field_validator("title")
    def validate_title(cls, title):
        if not title:
            raise ValueError("'title' must not be empty or None.")
        if len(title) > 50:
            raise ValueError("'title' are limited to 50 characters.")
        return title

    @field_validator("body")
    def validate_body(cls, body):
        if len(body) > 200:
            raise ValueError("'body' are limited to 200 characters.")
        return body

    @field_validator("photo")
    def validate_photo(cls, photo):
        try:
            if photo:
                encoded_photo = json.dumps(photo)
        except (json.JSONDecodeError, TypeError):
            raise ValueError("'photo' must be a valid JSON string")
        return encoded_photo

    @field_validator("tag")
    def validate_tag(cls, tag):
        try:
            if tag:
                encoded_tag = json.dumps(tag)
        except (json.JSONDecodeError, TypeError):
            raise ValueError("'tag' must be a valid JSON string")
        return encoded_tag

    class Config:
        from_attributes = True
