from fastapi import FastAPI
from routes import auth, workspace
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
from routes.workspace import router as workspace_router
app.include_router(auth.router)
app.include_router(workspace.router, prefix="/api/v1/workspace")
app.include_router(workspace_router, prefix="/api/v1/workspace", tags=["workspace"])
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)