from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import BlogPost
from app import db

blog_blueprint = Blueprint('blog_post', __name__)

# Create a new blog post
@blog_blueprint.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.json
    new_post = BlogPost(title=data['title'], content=data['content'], email=get_jwt_identity()['email'], user_id=get_jwt_identity()['user_id'])
    new_post.save()
    return jsonify({'message': 'Post created successfully', 'post_id': new_post.id}), 201

# Retrieve all blog posts
@blog_blueprint.route('/posts', methods=['GET'])
def get_all_posts():
    posts = BlogPost.query.all()
    posts_data = [{'id': post.id, 'title': post.title, 'content': post.content, 'email': post.email} for post in posts]
    return jsonify(posts_data)

# Retrieve a single blog post by ID
@blog_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post_data = {'id': post.id, 'title': post.title, 'content': post.content, 'email': post.email}
    return jsonify(post_data)

# Update an existing blog post
@blog_blueprint.route('/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    data = request.json
    post = BlogPost.query.get_or_404(post_id)
    
    if post.email != get_jwt_identity()['email']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'})

# Delete a blog post
@blog_blueprint.route('/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    
    if post.email != get_jwt_identity()['email']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    post.delete()
    return jsonify({'message': 'Post deleted successfully'}), 204
