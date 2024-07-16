# JWT Auth Blog Project

This project demonstrates a simple blog application using Flask with JWT (JSON Web Token) authentication. It allows users to register, login, create, read, update, and delete blog posts.

## Setup

### Prerequisites

- Python 3.x installed
- PostgreSQL installed and running
- Basic understanding of Flask and RESTful APIs

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/jwt-auth-blog.git
   cd jwt-auth-blog

2. Create and activate a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate      # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Set environment variables (optional, adjust as necessary):

   ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export SECRET_KEY='your_secret_key'
    export JWT_SECRET_KEY='your_jwt_secret_key'
    export DATABASE_URL='postgresql://username:password@localhost/dbname'

Replace your_secret_key, your_jwt_secret_key, and postgresql://username:password@localhost/dbname with appropriate values.

5. Initialize the database and run migrations:

   ```bash
    flask db init
    flask db migrate
    flask db upgrade

## Usage
### Running the Application

Start the Flask development server:

    ```bash
    flask run

The application will be available at http://localhost:5000.

## API Endpoints
### Authentication
 * Register User:
    ```bash
    curl -X POST http://localhost:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{"username": "john_doe", "password": "password123"}'

 * Login User:
    ```bash
    curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "john_doe", "password": "password123"}'

### Blog Posts
 * Create Post:
    ```bash
    curl -X POST http://localhost:5000/posts \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>" \
     -d '{"title": "New Post", "body": "This is the body of the new post."}'

 * Get All Posts:
    ```bash
     curl http://localhost:5000/posts

 * Get Single Post:
    ```bash
    curl http://localhost:5000/posts

 * Update Post:
    ```bash
    curl -X PUT http://localhost:5000/posts/<post_id> \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>" \
     -d '{"title": "Updated Post Title", "body": "Updated body of the post."}'

 * Delete Post:
    ```bash
    curl -X DELETE http://localhost:5000/posts/<post_id> \
     -H "Authorization: Bearer <YOUR_JWT_TOKEN>"

Replace <YOUR_JWT_TOKEN> and <post_id> with actual values obtained from the login endpoint and respective post ID.




