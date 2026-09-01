from app.database import db
from app.models.user import User

class UserSeeder:
    """
    Seeder class to populate default users in the database.
    """
    def run(self):
        # Check if default test admin user already exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            default_admin = User(name='Administrator', username='admin')
            default_admin.set_password('password123')
            db.session.add(default_admin)
            db.session.commit()
            print("[Seeder] Default administrator 'admin' successfully seeded.")
        else:
            print("[Seeder] Administrator 'admin' already exists. Skipping.")
