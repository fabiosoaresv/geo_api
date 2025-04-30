from fastapi import APIRouter
from app.schemas.user import User

user_router = APIRouter()

class UserController:
    @user_router.post("/users/")
    def create(user: User):
        return {
            "user": {
                "name": user.name,
                "email": user.email,
                "age": user.age
            }
        }


