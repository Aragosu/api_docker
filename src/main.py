from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from config import REDIS_HOST, REDIS_PORT

from auth.router import router as router_operation0
from operations.router import router as router_operation1
from operations.router import router2 as router_operation2

app = FastAPI(title="RecSys")

#авторизация
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=["Авторизация"]
)


# регистрация
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["Регистрация"]
)

app.include_router(router_operation0)
app.include_router(router_operation1)
app.include_router(router_operation2)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")