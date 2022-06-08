from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route
from stanforteedge.core import settings

# normal routes
from stanforteedge.src.app import index
from stanforteedge.src.app.gallery.view import gallery_page
from stanforteedge.src.app.team import view as team_routes
from stanforteedge.src.app.projects import view as project_routes

# admin routes
from stanforteedge.src.app.admin.routes import index as admin_index
from stanforteedge.src.app.admin.routes.auth import view as auth_routes

routers = [
    Mount("/static", app=StaticFiles(directory=settings.static_path), name="static"),
    Mount(
        path="/about",
        routes=[
            Route(
                path="/corporation-profile",
                endpoint=team_routes.corporation_profile,
                methods=["GET"],
                name="corporation_profile",
            ),
            Route(
                path="/management-team",
                endpoint=team_routes.management_team,
                methods=["GET"],
                name="management_team",
            ),
            Route(
                path="/board-or-director",
                endpoint=team_routes.board_or_director,
                methods=["GET"],
                name="board_or_director",
            ),
        ],
    ),
    Route(
        path="/admin",
        endpoint=admin_index.admin_dashboard,
        methods=["GET"],
        name="admin_homepage",
    ),
    Mount(
        path="/admin",
        routes=[
            Route(
                path="/",
                endpoint=admin_index.admin_dashboard,
                methods=["GET"],
                name="admin_homepage",
            ),
            Route(
                path="/login",
                endpoint=auth_routes.admin_login,
                methods=["GET"],
                name="admin_login",
            ),
            Route(
                path="/register",
                endpoint=auth_routes.admin_register,
                methods=["GET"],
                name="admin_register",
            ),
            Route(
                path="/forgot_password",
                endpoint=auth_routes.admin_forgot_password,
                methods=["GET"],
                name="admin_forgot_password",
            ),
            Route(
                path="/reset_password/{password_reset_token:str}",
                endpoint=auth_routes.admin_password_reset,
                methods=["GET"],
                name="admin_reset_password",
            ),
        ],
    ),
    Mount(
        path="/",
        routes=[
            Route(
                path="/projects",
                endpoint=project_routes.project_page,
                methods=["GET"],
                name="projects",
            ),
            Route(
                path="/contact",
                endpoint=index.conactpage,
                methods=["GET"],
                name="contact",
            ),
            Route(
                path="/",
                endpoint=index.homepage,
                methods=["GET"],
                name="homepage",
            ),
            Route(
                path="/gallery",
                endpoint=gallery_page,
                methods=["GET"],
                name="gallery",
            ),
        ],
    ),
]
