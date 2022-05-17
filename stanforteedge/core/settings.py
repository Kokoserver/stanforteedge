from starlette.config import Config as __Config
from stanforteedge.utils import base


__config = __Config(".env")

debug = __config("DEBUG", cast=str, default=False)
base_dir = __config("base_dir", cast=str, default=base.get_cwd())
template_path = __config("template_dir", cast=str, default=f"{base_dir}/src/templates")
static_path = __config("static_dir", cast=str, default=f"{base_dir}/src/static")
print(template_path)
