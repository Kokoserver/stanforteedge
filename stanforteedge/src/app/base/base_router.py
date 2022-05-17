from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route
from stanforteedge.src.app import index

routes = [
    Route(
        path="/",
        endpoint=index.homepage,
        methods=["GET"],
        name="homepage",
    )
]
