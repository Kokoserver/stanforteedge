from starlette.config import Config as __Config
from stanforteedge.utils import base


__config = __Config(".env")

debug = __config("DEBUG", cast=str, default=False)
base_dir = __config("base_dir", cast=str, default=base.get_cwd())
template_path = __config(
    "template_dir", cast=str, default=f"{base_dir}/src/frontend/templates"
)
static_path = __config(
    "static_dir", cast=str, default=f"{base_dir}/src/frontend/static"
)

secret_key = __config("SECRET_KEY", cast=str, default="***REPLACEME***")
crsf_key = __config("CRSf_KEY", cast=str, default="***REPLACEME***")

email_host = __config("EMAIL_HOST", cast=str, default="smtp.gmail.com")
email_port = __config("EMAIL_PORT", cast=int, default=587)
email_username = __config("EMAIL_HOST_USER", cast=str, default="you email")
email_password = __config("EMAIL_HOST_PASSWORD", cast=str, default="your password")
