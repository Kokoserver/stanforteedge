from uvicorn.main import run
from stanforteedge.core import settings


def run_app():
    run(
        "stanforteedge.main:app", reload=settings.debug, workers=4, debug=settings.debug
    )


if __name__ == "__main__":
    run_app()
