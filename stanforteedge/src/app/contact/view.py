from starlette.requests import Request
from stanforteedge.core.shortcut import reirect, render
from stanforteedge.src.app.contact.form import ContactForm
from stanforteedge.core import settings
from starlette import status
from starlette.background import BackgroundTask
import yagmail
from stanforteedge.core.shortcut import flash_message


def send_mail(to_email: str, subject: str, body: str):
    yag = yagmail.SMTP(user=settings.email_username, password=settings.email_password)
    task: BackgroundTask = BackgroundTask(
        yag.send, to=to_email, subject=subject, contents=body
    )
    return task


async def conactpage(request: Request):
    contact_form = await ContactForm.from_formdata(request)
    if request.method == "POST":
        if await contact_form.validate_on_submit():
            sender = send_mail(
                to_email=contact_form.email.data.lower(),
                subject="Contact from stanforteedge",
                body=contact_form.message.data,
            )
            flash_message.flash(
                request,
                "Thanks for contacting us, we will get in tourch soon",
            )
            return reirect(
                "/", status_code=status.HTTP_301_MOVED_PERMANENTLY, background=sender
            )
    return render(
        request,
        "pages/contact.html",
        context={"contact_form": contact_form},
    )
