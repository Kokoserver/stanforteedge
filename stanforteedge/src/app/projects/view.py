from starlette.requests import Request
from stanforteedge.core.shortcut import render


def project_enable_page(request: Request):
    return render(
        request,
        "pages/projects/project_enable.html",
    )

def lafiami_page(request: Request):
    return render(
        request,
        "pages/projects/lafiami.html",
    )

def checkNaija_page(request: Request):
    return render(
        request,
        "pages/projects/check_naija.html",
    )

def access360_page(request: Request):
    return render(
        request,
        "pages/projects/access360.html",
    )

def educard_page(request: Request):
    return render(
        request,
        "pages/projects/educard.html",
    )

def studentpad_page(request: Request):
    return render(
        request,
        "pages/projects/educard.html",
    )

def follow_dis_act_page(request: Request):
    return render(
        request,
        "pages/projects/follow_dis_act.html",
    )