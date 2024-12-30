from fastapi import FastAPI
from fastapi.params import Depends

from src.dependencies import validate_user_credentials
from src.schemas import (
    TokenInfo,
    Payload,
)
from src.config import settings
from src.utils import encode_jwt

app = FastAPI()


@app.post(
    settings.api_v1_prefix + "/login",
    response_model=TokenInfo,
)
def login(user: Payload = Depends(validate_user_credentials)):
    payload = {"sub": user.user_id}
    token = encode_jwt(payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )
