from starlette.requests import Request
from stanforteedge.core.shortcut import render


def project_page(request: Request):
    return render(
        request,
        "pages/projects/index.html",
    )
