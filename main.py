import logging as log
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlmodel import SQLModel
from admin import custom_model_view
from model.db_models import Sentinent, Stock
from flask_admin.contrib.sqla import ModelView
from repository.sentinent_repo import SentinentRepository
from repository.database import db
from config.appconfig import config

log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
log.getLogger("werkzeug").setLevel(log.CRITICAL)
log.getLogger("sqlalchemy.engine").setLevel(log.DEBUG)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = config.database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        SQLModel.metadata.drop_all(db.engine)
        SQLModel.metadata.create_all(db.engine)
        db.session.add(Stock(id="AMD",name="nev"))
        db.session.add(Sentinent(stock_id="AMD", rating=5))
        db.session.commit()
    admin = Admin(app, name="Admin", template_mode="bootstrap3")
    admin.add_view(custom_model_view.CustomModelView(Sentinent, db.session))
    admin.add_view(custom_model_view.CustomModelView(Stock, db.session))
    app.run(debug=True)