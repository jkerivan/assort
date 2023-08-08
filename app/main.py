from fastapi import FastAPI
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette_context.middleware import RawContextMiddleware
import logging
from app.api import routers 

def get_application() -> FastAPI:

    ALLOWED_HOSTS = ["*"]

    app = FastAPI(title="Assort Project", debug=True, middleware=[
        Middleware(CORSMiddleware, allow_origins=ALLOWED_HOSTS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]),
        Middleware(RawContextMiddleware)
    ])

    app.include_router(routers.router) 

    return app

app = get_application()