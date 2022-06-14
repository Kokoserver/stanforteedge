from starlette.requests import Request
from stanforteedge.core.shortcut import render


def corporation_profile(request: Request):
    return render(
        request,
        "pages/about/corporation_profile.html",
    )


def management_team(request: Request):
    return render(
        request,
        "pages/about/management_team.html",
    )


def board_or_director(request: Request):
    return render(
        request,
        "pages/about/board_or_director.html",
    )
