from typing import Mapping, Optional
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.background import BackgroundTask
from starlette import status
from stanforteedge.core import settings


def render(
    request: Request,
    template_name: str,
    background: Optional[BackgroundTask] = None,
    headers: Optional[Mapping[str, str]] = None,
    status_code: Optional[int] = status.HTTP_200_OK,
    context: Optional[dict] = {},
):
    template_dir = Jinja2Templates(directory=settings.template_path, auto_reload=True)
    ctx = context.copy()
    ctx.update({"request": request})
    return template_dir.TemplateResponse(
        name=template_name,
        context=ctx,
        status_code=status_code,
        headers=headers,
        media_type="text/html",
        background=background,
    )
