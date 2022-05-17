from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.requests import Request
from stanforteedge.core import settings
from stanforteedge.core.shortcut import render


app = Starlette(debug=settings.debug)


@app.route("/", methods=["GET"])
async def add_user(request: Request):
    return render(
        request,
        "index.html",
    )
