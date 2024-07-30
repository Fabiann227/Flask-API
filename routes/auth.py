from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import get_db_connection

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username diperlukan')
        parser.add_argument('password', type=str, required=True, help='Password diperlukan')
        parser.add_argument('email', type=str, required=True, help='Email diperlukan')
        args = parser.parse_args()

        hashed_password = generate_password_hash(args['password'], method='pbkdf2:sha256')
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (args['username'],))
        if cursor.fetchone():
            return {'message': 'Username sudah digunakan'}, 400

        if '@' not in args['email']:
            return {'message': 'Email tidak valid'}, 400

        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
                       (args['username'], hashed_password, args['email']))
        conn.commit()
        cursor.close()
        conn.close()
        return {'message': 'User berhasil terdaftar'}, 201

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username diperlukan')
        parser.add_argument('password', type=str, required=True, help='Password diperlukan')
        args = parser.parse_args()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (args['username'],))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if not user or not check_password_hash(user[2], args['password']):
            return {'message': 'Password salah'}, 401

        access_token = create_access_token(identity={'username': args['username']})
        return {'access_token': access_token}, 200
