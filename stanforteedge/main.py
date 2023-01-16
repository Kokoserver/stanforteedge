from starlette.applications import Starlette
from .core import settings
from .src.app.base import base_router
# from db.config import app_startup
from .core import middleware

app = Starlette(
    debug=settings.debug, routes=base_router.routers, middleware=middleware.wares
)


# @app.on_event("startup")
# def start_up():
#     app_startup(app)
#     print("app is starting up")
