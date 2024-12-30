from fastapi.params import Depends

from src.exeptions import UnauthenticatedUserHTTPException
from src.schemas import InputData, Payload
from src.utils import validate_password, decode_jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


def validate_user_credentials(user_input_data: InputData) -> Payload:
    """
    Валидация логина и пароля, присланные пользователем. При
    успешной валидации возвращается payload для токена
    """
    user = ...  #  TODO: запрос в БД на получение пользователя по логину
    if not user or not validate_password(user_input_data.password, user.password):
        raise UnauthenticatedUserHTTPException
    return Payload(user_id=user.id)


def get_current_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> dict:
    token = credentials.credentials
    payload = decode_jwt(token)
    return payload


def get_current_auth_user(payload: dict = Depends(get_current_token_payload)) -> dict:
    user = ...  # TODO: сделать запрос в БД по id пользователя из payload (поле "sub")
    return user
