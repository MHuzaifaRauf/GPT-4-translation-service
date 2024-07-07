from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    language: list[str]


class TranslateResponse(BaseModel):
    translate_id: int


class TranslateStatus(BaseModel):
    translate_id: int
    status: str
    translations: dict[str, str]