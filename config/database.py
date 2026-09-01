import os
from dotenv import load_dotenv

# Load .env file from the root directory
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

class DatabaseConfig:
    """
    Database configuration manager loaded from environmental variables.
    """
    CONNECTION = os.getenv('DB_CONNECTION', 'mysql')
    HOST = os.getenv('DB_HOST', '127.0.0.1')
    PORT = os.getenv('DB_PORT', '3306')
    DATABASE = os.getenv('DB_DATABASE', 'raptor_db')
    USERNAME = os.getenv('DB_USERNAME', 'root')
    PASSWORD = os.getenv('DB_PASSWORD', '')

    @classmethod
    def get_sqlalchemy_uri(cls):
        """
        Generate SQLAlchemy database connection URI.
        """
        if cls.CONNECTION == 'mysql':
            # Use PyMySQL driver for pure Python MySQL connectivity
            return f"mysql+pymysql://{cls.USERNAME}:{cls.PASSWORD}@{cls.HOST}:{cls.PORT}/{cls.DATABASE}"
        # Fallback to SQLite database if connection is sqlite
        return "sqlite:///raptor.db"
