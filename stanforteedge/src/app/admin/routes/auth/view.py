from starlette.requests import Request
from stanforteedge.core.shortcut import render


def admin_login(request: Request):
    return render(
        request,
        "admin/pages/auth/login.html",
    )


def admin_register(request: Request):
    return render(
        request,
        "admin/pages/auth/register.html",
    )


def admin_password_reset(request: Request):
    return render(
        request,
        "admin/pages/auth/resetpassword.html",
    )


def admin_forgot_password(request: Request):
    return render(
        request,
        "admin/pages/auth/forgotpassword.html",
    )
