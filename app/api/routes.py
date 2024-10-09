from fastapi import APIRouter
from app.api.endpoints import preferences, notifications, users

def get_router():

    router = APIRouter()

    router.include_router(preferences.router, prefix="/preferences", tags=["preferences"])
    router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
    router.include_router(users.router, prefix="/users", tags=["users"])

    return router