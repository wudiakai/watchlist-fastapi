from fastapi import APIRouter
from tortoise.contrib.fastapi import register_tortoise

from .endpoints import *

v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(user)
v1.include_router(movie)



