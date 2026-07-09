from app.database import db

class CreateUsersTable:
    """
    Migration class to create and drop the 'users' table.
    """
    def up(self):
        """
        Run the migration to create the table.
        """
        db.session.execute(db.text("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                INDEX idx_users_username (username)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """))
        db.session.commit()

    def down(self):
        """
        Reverse the migration by dropping the table.
        """
        db.session.execute(db.text("DROP TABLE IF EXISTS users"))
        db.session.commit()
