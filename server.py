from uvicorn import run
from stanforteedge.core import settings


def run_app():
    run("main:app", reload=settings.debug, workers=4)


if __name__ == "__main__":
    run_app()
