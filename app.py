from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
from routes.auth import Register, Login
from routes.protected import ProtectedResource
from openapi import generate_openapi_spec
from models import create_tables

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

api = Api(app)
api.add_resource(Register, '/api/register')
api.add_resource(Login, '/api/login')
api.add_resource(ProtectedResource, '/api/protected')

@app.route('/')
def root():    
    return "Hello"

@app.route('/api/swagger.json')
def serve_openapi_spec():
    spec = generate_openapi_spec()
    return jsonify(spec)

SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "API Autentikasi Pengguna"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
