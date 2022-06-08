from starlette.requests import Request
from stanforteedge.core.shortcut import render


def gallery_page(request: Request):
    return render(
        request,
        "pages/gallery.html",
    )
