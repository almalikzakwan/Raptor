from database.seeders.user_seeder import UserSeeder

class DatabaseSeeder:
    """
    Central database seeder class that runs all registered model seeders.
    """
    def run(self):
        # Run specific model seeders sequentially
        UserSeeder().run()
