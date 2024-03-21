from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from auth.base_config import current_user
from auth.models import User
from ml_model.LightFMClass import model_recomend, genre_list

router = APIRouter(tags=["Основной сервис (для авторизованных пользователей)"])
router2 = APIRouter(tags=["Основной сервис (для новых пользователей)"])


@router.get("/rec_auth")
@cache(expire=30)
async def give_rec(user: User = Depends(current_user)):
    return model_recomend(user.id, None)


@router.post("/rec_genre_auth")
async def give_rec_genre(genre: str, user: User = Depends(current_user)):
    if genre.title() not in genre_list:
        raise HTTPException(status_code=404, detail=f"Неправильный жанр, вы можете выбрать: {genre_list}")
    return model_recomend(user.id, genre)


@router2.get("/rec_nonauth")
@cache(expire=30)
async def give_rec():
    return model_recomend(123456789, None)


@router2.post("/rec_genre_nonauth")
async def give_rec_genre(genre: str):
    if genre.title() not in genre_list:
        raise HTTPException(status_code=404, detail=f"Неправильный жанр, вы можете выбрать: {genre_list}")
    return model_recomend(123456789, genre)
