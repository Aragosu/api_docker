from fastapi import APIRouter, Depends
from auth.base_config import current_user
from auth.models import User

router = APIRouter(tags=["Авторизация"])


@router.get("/")
async def who_am_i(user: User = Depends(current_user)):
    return f'Имя пользователя: {user.username}, email: {user.email}, id: {user.id}'
