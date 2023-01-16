# from stanforteedge.src.app.base import base_model
# from tortoise.contrib.starlette import register_tortoise
# from stanforteedge.core import settings

# def app_startup(app):
#     try:
#         register_tortoise(
#             app,
#             db_url=settings.db_url,
#             modules={"models": base_model.models_list},
#             generate_schemas=True,
#         )
#         print("db is connected successuflly")
#     except:
#         print("error connecting to db")
