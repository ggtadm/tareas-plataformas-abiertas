
from flask import Flask, redirect
from flask_cors import CORS
from .controllers.estudiantes import estudiantes_endpoints

def create_app():
    app = Flask(__name__)

    # Rutas bajo /estudiantes/api/v1
    app.register_blueprint(
        estudiantes_endpoints,
        url_prefix="/estudiantes/api/v1"
    )

    # Rutas directas (/hola, /saludo) por si se consultan directamente
    app.register_blueprint(
        estudiantes_endpoints,
        url_prefix="",
        name="estudiantes_directo"
    )

    CORS(app, origins="*")

    @app.route('/')
    def index():
        return redirect('/estudiantes/api/v1/hola')

    return app
