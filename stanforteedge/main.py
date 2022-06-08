from starlette.applications import Starlette
from stanforteedge.core import settings
from stanforteedge.src.app.base import base_router
from stanforteedge.db.config import app_startup

app = Starlette(debug=settings.debug, routes=base_router.routers)

# @app.on_event("startup")
# def start_up():
#     app_startup(app)
#     print("app is starting up")
