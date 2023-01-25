from pydantic import BaseModel, HttpUrl

# This file contains the pydantic models that can be used for validation purposes


class Input(BaseModel):
    # this will do full validation (scheme, top level domain, host)
    url: HttpUrl
    description: str = ''


class MetaData(BaseModel):
    long_url: str
    short_url: str
    klicks: int = 0
    created: str
    description: str = ''

    # orm mode tells pydantic to read data even if not from a dict but an orm model
    class Config:
        orm_mode = True
