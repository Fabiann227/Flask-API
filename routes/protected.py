from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'message': f'Hello, {current_user["username"]}! Anda telah mengakses resource yang dilindungi.'}, 200
