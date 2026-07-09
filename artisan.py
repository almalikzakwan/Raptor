import os
import sys
import importlib
import datetime
from route.web import app
from app.database import db

def init_migrations_table():
    """
    Ensure the migrations tracking table exists in the database.
    """
    db.session.execute(db.text("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            migration VARCHAR(255) NOT NULL,
            batch INT NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """))
    db.session.commit()

def run_migrations():
    """
    Run all pending migrations.
    """
    print("[Artisan] Running migrations...")
    try:
        init_migrations_table()
    except Exception as e:
        print(f"[Artisan Error] Could not connect to database or create migrations table: {e}")
        return

    # Get already executed migrations
    result = db.session.execute(db.text("SELECT migration FROM migrations"))
    executed = {row[0] for row in result.fetchall()}

    # List all migration files
    migrations_dir = os.path.join(os.path.dirname(__file__), 'database/migrations')
    if not os.path.exists(migrations_dir):
        print("[Artisan Warning] Migrations directory does not exist.")
        return

    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.py') and f != '__init__.py'])

    pending = [f for f in migration_files if f not in executed]

    if not pending:
        print("[Artisan] Nothing to migrate.")
        return

    # Determine next batch number
    result = db.session.execute(db.text("SELECT MAX(batch) FROM migrations"))
    max_batch = result.fetchone()[0]
    next_batch = (max_batch or 0) + 1

    for file_name in pending:
        print(f"Migrating: {file_name}")
        module_name = f"database.migrations.{file_name[:-3]}"
        
        # Dynamically import the module
        module = importlib.import_module(module_name)

        # Retrieve the migration class defined in the module
        migration_class = None
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and attr.__module__ == module_name:
                migration_class = attr
                break

        if not migration_class:
            print(f"[Artisan Error] Could not find migration class in: {file_name}")
            continue

        # Execute migration logic
        migration_instance = migration_class()
        try:
            migration_instance.up()
            # Log successful migration batch execution
            db.session.execute(
                db.text("INSERT INTO migrations (migration, batch) VALUES (:migration, :batch)"),
                {"migration": file_name, "batch": next_batch}
            )
            db.session.commit()
            print(f"Migrated:  {file_name}")
        except Exception as err:
            db.session.rollback()
            print(f"[Artisan Error] Failed to migrate {file_name}: {err}")
            break

def rollback_migrations():
    """
    Rollback the last batch of migrations.
    """
    print("[Artisan] Rolling back migrations...")
    try:
        init_migrations_table()
    except Exception as e:
        print(f"[Artisan Error] Could not connect to database: {e}")
        return

    # Get the last batch number
    result = db.session.execute(db.text("SELECT MAX(batch) FROM migrations"))
    last_batch = result.fetchone()[0]

    if not last_batch:
        print("[Artisan] Nothing to rollback.")
        return

    # Get migrations in the last batch (reversing execution order)
    result = db.session.execute(
        db.text("SELECT migration FROM migrations WHERE batch = :batch ORDER BY id DESC"),
        {"batch": last_batch}
    )
    migrations_to_rollback = [row[0] for row in result.fetchall()]

    for file_name in migrations_to_rollback:
        print(f"Rolling back: {file_name}")
        module_name = f"database.migrations.{file_name[:-3]}"
        module = importlib.import_module(module_name)

        migration_class = None
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and attr.__module__ == module_name:
                migration_class = attr
                break

        if not migration_class:
            print(f"[Artisan Error] Could not find migration class in: {file_name}")
            continue

        # Revert migration logic
        migration_instance = migration_class()
        try:
            migration_instance.down()
            # Delete record from migrations log table
            db.session.execute(
                db.text("DELETE FROM migrations WHERE migration = :migration"),
                {"migration": file_name}
            )
            db.session.commit()
            print(f"Rolled back:  {file_name}")
        except Exception as err:
            db.session.rollback()
            print(f"[Artisan Error] Failed to rollback {file_name}: {err}")
            break

def seed_database():
    """
    Run database seeders.
    """
    print("[Artisan] Seeding database...")
    try:
        from database.seeders.database_seeder import DatabaseSeeder
        seeder = DatabaseSeeder()
        seeder.run()
    except Exception as e:
        print(f"[Artisan Error] Failed to seed database: {e}")

def make_migration(name):
    """
    Create a new migration file stub.
    """
    if not name:
        print("[Artisan Error] Migration name is required (e.g. python artisan.py make:migration create_users_table)")
        return

    timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')
    file_name = f"{timestamp}_{name}.py"
    migrations_dir = os.path.join(os.path.dirname(__file__), 'database/migrations')
    os.makedirs(migrations_dir, exist_ok=True)
    file_path = os.path.join(migrations_dir, file_name)

    # Convert snake_case name to PascalCase for the class definition
    class_name = "".join(part.capitalize() for part in name.split('_'))

    template = f"""from app.database import db

class {class_name}:
    def up(self):
        \"\"\"
        Run the migrations.
        \"\"\"
        # Write schema creations here (e.g. db.session.execute(db.text("...")))
        pass

    def down(self):
        \"\"\"
        Reverse the migrations.
        \"\"\"
        # Write schema drops here
        pass
"""

    with open(file_path, 'w') as f:
        f.write(template)

    print(f"[Artisan] Created Migration: database/migrations/{file_name}")

def make_seeder(name):
    """
    Create a new seeder file stub.
    """
    if not name:
        print("[Artisan Error] Seeder name is required (e.g. python artisan.py make:seeder user_table_seeder)")
        return

    # Suffix name automatically with '_seeder' if not present
    if not name.endswith('seeder') and not name.endswith('Seeder'):
        name = name + '_seeder'

    # Convert to PascalCase for class definition
    class_name = "".join(part.capitalize() for part in name.split('_'))
    file_name = f"{name.lower()}.py"
    seeders_dir = os.path.join(os.path.dirname(__file__), 'database/seeders')
    os.makedirs(seeders_dir, exist_ok=True)
    file_path = os.path.join(seeders_dir, file_name)

    template = f"""from app.database import db

class {class_name}:
    def run(self):
        \"\"\"
        Run the database seeds.
        \"\"\"
        # Write model seeding code here
        pass
"""

    with open(file_path, 'w') as f:
        f.write(template)

    print(f"[Artisan] Created Seeder: database/seeders/{file_name}")

def show_help():
    print("""
Raptor Framework CLI (Artisan equivalent)

Usage:
  python artisan.py <command> [arguments]

Available commands:
  migrate             Run all pending migrations
  migrate:rollback    Rollback the last batch of migrations
  db:seed             Run all database seeders
  make:migration      Create a new migration file stub (e.g. python artisan.py make:migration create_posts_table)
  make:seeder         Create a new seeder file stub (e.g. python artisan.py make:seeder posts_table_seeder)
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    command = sys.argv[1]

    with app.app_context():
        if command == "migrate":
            run_migrations()
        elif command == "migrate:rollback":
            rollback_migrations()
        elif command == "db:seed":
            seed_database()
        elif command == "make:migration":
            name = sys.argv[2] if len(sys.argv) > 2 else None
            make_migration(name)
        elif command == "make:seeder":
            name = sys.argv[2] if len(sys.argv) > 2 else None
            make_seeder(name)
        else:
            print(f"Unknown command: {command}")
            show_help()
