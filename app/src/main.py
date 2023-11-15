

from fastapi import FastAPI
from app.src.adverts.router import router as router_adverts
from app.src.users.router import router as router_users


app = FastAPI()
app.include_router(router_users)
app.include_router(router_adverts)
