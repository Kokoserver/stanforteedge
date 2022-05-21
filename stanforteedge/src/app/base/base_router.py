from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route
from stanforteedge.src.app import index
from stanforteedge.core import settings

routes = [
    Mount("/static", app=StaticFiles(directory=settings.static_path), name="static"),
    Route(
        path="/",
        endpoint=index.homepage,
        methods=["GET"],
        name="homepage",
    ),
]
