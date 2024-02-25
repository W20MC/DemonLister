from fastapi.responses import RedirectResponse
from flask import Flask
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.openapi.utils import get_openapi

from routes import home, challenge
from routes.fastapi import api

flask_app = Flask(__name__)
flask_app.register_blueprint(home.home)
flask_app.register_blueprint(challenge.challenge)

app = FastAPI()
app.mount("/list", WSGIMiddleware(flask_app))
app.include_router(api.router)

@app.get("/")
def main():
    return RedirectResponse("/list/")

def openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title = "DemonLister",
        version = "1.0.0",
        routes = app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = openapi