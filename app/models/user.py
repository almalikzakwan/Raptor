from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    User database model representing users in the MySQL table.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """
        Hash and set the user's password.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify the user's password against the stored hash.
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"
