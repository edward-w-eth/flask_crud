from datetime import datetime
from app import db
from app.base_model import BaseModel

class BlogPost(BaseModel):
    """This class defines blog_posts table"""
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, content, email, user_id):
        self.title = title
        self.content = content
        self.email = email
        self.user_id = user_id
