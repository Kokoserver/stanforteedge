from starlette.requests import Request
from stanforteedge.core.shortcut import render
from  stanforteedge.src.app.admin.routes.auth.form import  RegisterForm, LoginForm

async def admin_login(request: Request):
    login_form = await LoginForm.from_formdata(request)
    return render(
        request,
        "admin/pages/auth/login.html",
        context={'login_form': login_form}
      
    )


async def admin_register(request: Request):
    register_form = await RegisterForm.from_formdata(request)
    return render(
        request,
        "admin/pages/auth/register.html",
          context={'register_form': register_form}
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
