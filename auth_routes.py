from fastapi import APIRouter


auth_router = APIRouter(
    prefix='/auth',
    tags=['author']
)


@auth_router.get('/')
async def hello():
    return {'message': 'Hello'}