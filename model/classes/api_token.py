from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ApiToken(BaseModel):
    api_key: str = Field(max_length=50)
    api_secret_key: str = Field(max_length=50)
    datetime_of_issue: str
    effective_datetime: str
    delete_flg: Optional[bool] = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @field_validator("api_key")
    def validate_api_key(cls, key):
        if not key:
            raise ValueError("'api_key' must not be empty or None.")
        if len(key) > 50:
            raise ValueError("'api_key' are limited to 50 characters.")
        return key

    @field_validator("api_secret_key")
    def validate_api_secret_key(cls, key):
        if not key:
            raise ValueError("'api_secret_key' must not be empty or None.")
        if len(key) > 50:
            raise ValueError("'api_secret_key' are limited to 50 characters.")
        return key

    @field_validator("datetime_of_issue")
    def validate_datetime_of_issue(cls, dateTime):
        if not dateTime:
            raise ValueError("'datetime_of_issue' must not be empty or None.")
        return dateTime

    @field_validator("effective_datetime")
    def validate_effective_datetime(cls, dateTime):
        if not dateTime:
            raise ValueError("'effective_datetime' must not be empty or None.")
        return dateTime
