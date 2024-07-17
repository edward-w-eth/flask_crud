from datetime import datetime
from flask_bcrypt import Bcrypt
from app import db
from app.base_model import BaseModel
from app.blog_post.models import BlogPost
import jwt

class User(BaseModel):
    """This class defines users table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __init__(self, email, password):
        """Initialize the user with the user details"""
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()

    def password_is_valid(self, password):
        """Check the password against its hash"""
        return Bcrypt().check_password_hash(self.password, password)