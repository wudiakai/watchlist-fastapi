from fastapi import APIRouter

user = APIRouter(tags=["用户相关"])


@user.get("/login", summary="当前用户")
async def user_info():
    pass


@user.put("/login", summary="修改用户")
async def user_update():
    pass


__all__=[
    "user"
]