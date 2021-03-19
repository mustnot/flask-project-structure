from pydantic import BaseModel, validator
from pydantic import conint, constr
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserManager(BaseModel):
    email: constr(strip_whitespace=True, max_length=100, regex="")
    username: constr(strip_whitespace=True, min_length=4, max_length=100)
    password: constr(min_length=10, max_length=100)

    @validator("email")
    def normalize_email(cls, v):
        return v.lower()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    def __init__(self, email, username, **kwargs):
        self.email = email
        self.username = username
    

    def __repr__(self) -> str:
        return f"<User('{self.username}', '{self.email}')>"


    def set_password(self, password) -> str:
        self.password = generate_password_hash(password)
        return self

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)
    
    def create(self):
        db.session.add(self)
        db.session.commit()
