from flask import Flask
from flask_migrate import Migrate
from investportfolioapp.database.db_init import db
from investportfolioapp.routes import *

app = Flask(__name__, 
            static_url_path='', 
            static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:password@host.docker.internal:5432/app_db"
db.init_app(app)
migrate = Migrate(app, db)

register_routes(app, db)

