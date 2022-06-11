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
crsf_key = __config("CSRF_KEY", cast=str, default="***REPLACEME***")

db_username = __config('DB_NAME', cast=str, default='')
db_password = __config('DB_PASSWORD', cast=str, default='')
db_host = __config('DB_HOST', cast=str, default='localhost')
db_name = __config('DB_NAME', cast=str, default='')
db_url = f'postgres://{db_username}:{db_password}@{db_host}/{db_name}'
