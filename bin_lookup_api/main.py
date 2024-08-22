from fastapi import FastAPI

from .application import start_application
from .settings import settings

app: FastAPI = FastAPI(
    title=settings.project.name,
    description=settings.project.description,
    version=settings.project.version,
)
start_application(app)

#uvicorn.run("bin_lookup_api.main:bin_lookup_api", host="127.0.0.1", port=8000, log_config=None, log_level="info")
