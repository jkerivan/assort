from app.api.endpoints.call import CallContext
from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette_context.middleware import RawContextMiddleware
import logging
from app.api import routers 
from starlette.middleware.base import BaseHTTPMiddleware
import contextvars


call_context_var = contextvars.ContextVar("call_context", default=None)

def get_call_context():
    return call_context_var.get()

logging.basicConfig()
logger = logging.getLogger(__name__)

class InitCallContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        call_context = CallContext()
        call_context_var.set(call_context)
        response = await call_next(request)
        return response

def get_application() -> FastAPI:

    ALLOWED_HOSTS = ["*"]

    app = FastAPI(title="Assort Project", debug=True, middleware=[
        Middleware(CORSMiddleware, allow_origins=ALLOWED_HOSTS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]),
        Middleware(RawContextMiddleware),
        Middleware(InitCallContextMiddleware)
    ])

    app.include_router(routers.router) 

    return app

app = get_application()