from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class BASE(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=BASE)