from flask import Flask
from route.router import Route
from config.database import DatabaseConfig
from app.database import db

# Import Controllers
from app.controllers.home_controller import HomeController
from app.controllers.auth_controller import AuthController
from app.controllers.dashboard_controller import DashboardController

app = Flask(__name__, template_folder='../views', static_folder='../static')

# Set application configurations from config database manager
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseConfig.get_sqlalchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'raptor_secret_key_change_me_in_production'

# Initialize shared SQLAlchemy database instance
db.init_app(app)

# Initialize Laravel-style Route engine
Route.init_app(app)



# --------------------------------------------------------------------------
# Register Routes (Laravel-style syntax)
# --------------------------------------------------------------------------

# Homepage Route
Route.get('/', [HomeController, 'index'], endpoint='home')

# Authentication Routes
Route.get('/login', [AuthController, 'show_login'], endpoint='login')
Route.post('/login', [AuthController, 'login'], endpoint='login_action')
Route.get('/logout', [AuthController, 'logout'], endpoint='logout')

# Protected Routes (Grouped or route-level middleware)
Route.middleware('auth').get('/dashboard', [DashboardController, 'index'], endpoint='dashboard')
