from starlette.requests import Request
from stanforteedge.core.shortcut import render


def admin_dashboard(request: Request):
    return render(
        request,
        "admin/pages/index.html",
    )
