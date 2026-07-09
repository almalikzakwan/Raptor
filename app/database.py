from flask_sqlalchemy import SQLAlchemy

# Instantiate central SQLAlchemy object to be shared by all models to avoid circular imports.
db = SQLAlchemy()
