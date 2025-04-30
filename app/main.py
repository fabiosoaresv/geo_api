from fastapi import FastAPI
from app.controllers.geo_api_controller import geo_api_router
from app.controllers.user_controller import user_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(geo_api_router)
app.include_router(user_router)
