from fastapi import FastAPI
from bin_lookup_api.lifespan import lifespan
from bin_lookup_api.routes import include_routers


def start_application(app: FastAPI):
    """
    Start the application launching all required modules
    """

    # ----------------------------------------
    # Middlewares
    # ----------------------------------------

    # Add middlewares (in order of desired execution)

    # ----------------------------------------
    # Lifespan (startup/shutdown async actions)
    # ----------------------------------------
    app.router.lifespan_context = lifespan

    # ----------------------------------------
    # Application routers
    # ----------------------------------------

    include_routers(app)

    return app
