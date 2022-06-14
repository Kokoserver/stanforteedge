from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware, CSRFProtectMiddleware
from stanforteedge.core import settings
wares = [
      Middleware(SessionMiddleware, secret_key=settings.secret_key),
    Middleware(CSRFProtectMiddleware, csrf_secret=settings.crsf_key)
]