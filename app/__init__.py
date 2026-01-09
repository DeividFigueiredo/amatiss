from flask import Flask, Blueprint
from app.routes.dwalt import dwalt_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(dwalt_bp, url_prefix= '/dwalt-eenv')

    return app