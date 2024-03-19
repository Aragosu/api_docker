import time

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
#from auth.base_config import current_user
#from auth.models import User
from operations.models import operation
from operations.schemas import OperationCreate

from ml_model.LightFMClass import model_recomend

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

router2 = APIRouter(
    prefix="/test2",
    tags=["Operation2"]
)

@router.get("/long_operation")
#@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    # https://stackoverflow.com/questions/76322342/fastapi-sqlalchemy-cannot-convert-dictionary-update-sequence-element-0-to-a-seq
    return result.scalars().all()


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()  # пробуем закомментировать
    return {"status": "success"}


@router.get("/test_MODEL_all_films")
@cache(expire=60)
async def all_rec():
#    lfm = LightFMRecSyc(model=ClassRecSyc,
#                        RecSycFilms=RecSycFilms,
#                        IMDb_df=moveis_fin,
#                        Genre=None)
#    result = lfm.recommend(user_id=[123456789], k=5, movies_to_predict=movies_to_predict)
    return 'pass'

@router2.post("/test_MODEL_choose_genre")
#@cache(expire=60)
async def genre_chose(id:int,genre: str):#: ChooseGenre):
    return model_recomend(id, genre)


#@router2.post("/test2")
#@cache(expire=60)
#async def test_id_current_user(user: User = Depends(current_user)):
#    return f'{user.username},{user.id}'


#@router.get("/main")
#async def main(session: AsyncSession = Depends(get_async_session)):
#    result = await session.execute(select(1))
#    return result.all()

