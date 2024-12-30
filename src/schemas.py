from annotated_types import MinLen
from pydantic import BaseModel, ConfigDict
from typing_extensions import Annotated


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


class Payload(BaseModel):
    user_id: int  # TODO: обсудить тип данных id пользователей в БД


class InputData(BaseModel):
    # Отключение конвертации входных параметров. Строгое соответствие типов
    model_config = ConfigDict(strict=True)

    login: Annotated[str, MinLen(1)]
    password: str
