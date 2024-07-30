from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default-secret')
    DB_CONFIG = {
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'app')
    }
