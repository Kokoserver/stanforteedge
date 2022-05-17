from starlette.requests import Request
from stanforteedge.core.shortcut import render


def homepage(request: Request):
    return render(
        request,
        "index.html",
    )
