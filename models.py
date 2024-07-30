import mysql.connector
from config import Config

def get_db_connection():
    return mysql.connector.connect(**Config.DB_CONFIG)

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
