from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route
from stanforteedge.core import settings

# normal routes
from stanforteedge.src.app import index
from stanforteedge.src.app.gallery.view import gallery_page
from stanforteedge.src.app.team import view as team_routes
from stanforteedge.src.app.projects import view as project_routes
from stanforteedge.src.app.contact import view as contact_routes

# admin routes
from stanforteedge.src.app.admin.routes import index as admin_index
from stanforteedge.src.app.admin.routes.auth import view as auth_routes

routers = [
    Mount("/static", app=StaticFiles(directory=settings.static_path), name="static"),
     Mount(
        path="/project",
        routes=[
            Route(
                path="/",
                endpoint=index.homepage,
                methods=["GET"],
                name="homepage",
            ),
            Route(
                path="/project_enable",
                endpoint=project_routes.project_enable_page,
                methods=["GET"],
                name="project_enable_page",
            ),
            Route(
                path="/lafiami",
                endpoint=project_routes.lafiami_page,
                methods=["GET"],
                name="lafiami_page",
            ),
            Route(
                path="/check_naija",
                endpoint=project_routes.checkNaija_page,
                methods=["GET"],
                name="checknaija_page",
            ),
             Route(
                path="/follow_dis_act",
                endpoint=project_routes.follow_dis_act_page,
                methods=["GET"],
                name="follow_dis_act_page",
            ),
            #  Route(
            #     path="/access360",
            #     endpoint=project_routes.access360_page,
            #     methods=["GET"],
            #     name="access360_page",
            # ),
            # Route(
            #     path="/educard",
            #     endpoint=project_routes.educard_page,
            #     methods=["GET"],
            #     name="educard_page",
            # ),
            Route(
                path="/studentpad",
                endpoint=project_routes.studentpad_page,
                methods=["GET"],
                name="studentpad_page",
            ),
        ],
    ),
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
            # Route(
            #     path="/board-or-director",
            #     endpoint=team_routes.board_or_director,
            #     methods=["GET"],
            #     name="board_or_director",
            # ),
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
                methods=["GET", "POST"],
                name="admin_login",
            ),
            Route(
                path="/register",
                endpoint=auth_routes.admin_register,
                methods=["GET", "POST"],
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
                path="/contact",
                endpoint=contact_routes.conactpage,
                methods=["GET", "POST"],
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
