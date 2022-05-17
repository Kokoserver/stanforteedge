from starlette.applications import Starlette
from stanforteedge.core import settings
from stanforteedge.src.app.base import base_router

app = Starlette(debug=settings.debug, routes=base_router.routes)
