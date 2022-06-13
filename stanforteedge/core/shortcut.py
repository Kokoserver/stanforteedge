from typing import Mapping, Optional
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.background import BackgroundTask
from starlette import status
from stanforteedge.core import settings
from stanforteedge.utils import flash_message


def render(
    request: Request,
    template_name: str,
    background: Optional[BackgroundTask] = None,
    headers: Optional[Mapping[str, str]] = None,
    status_code: Optional[int] = status.HTTP_200_OK,
    context: Optional[dict] = {},
):
    template_dir = Jinja2Templates(directory=settings.template_path, auto_reload=True)
    template_dir.env.globals['get_flashed_messages'] = flash_message.get_flashed_messages
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


def reirect(url:str, status_code:int=status.HTTP_302_FOUND,  headers: Mapping[str, str] = None,  background:Optional[BackgroundTask]=None):
    return RedirectResponse(url, status_code=status_code, headers=headers,  background=background)
    