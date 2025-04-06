import uvicorn
from fastapi import FastAPI

from app.core.db import init_db
from app.routers.auth_router import auth_router
from app.routers.post_router import post_router

app = FastAPI()
init_db()
app.include_router(auth_router)
app.include_router(post_router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)