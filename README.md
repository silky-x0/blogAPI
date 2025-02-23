# Flask REST API Learning Project

This is a learning project focused on building RESTful APIs using Flask. The project serves as a stepping stone towards creating a more complex blog API.

## Current Features
- Basic Flask application setup
- SQLAlchemy integration for database management
- User model implementation
- Basic routing examples

## Technical Stack
- Flask
- Flask-SQLAlchemy
- Flask-RESTful
- SQLite database

## Project Structure
```
Flask-api/
│
├── api.py          # Main application file
├── create_db.py    # Database initialization script
└── database.db     # SQLite database
```

## Learning Goals
- Understanding REST API principles
- Working with Flask and its extensions
- Database modeling with SQLAlchemy
- API resource handling
- Request parsing and validation

## Next Steps
- Implementing CRUD operations
- Adding authentication
- Building a full-featured blog API
- Adding proper error handling
- Implementing API documentation

## Getting Started
1. Install dependencies:
```bash
pip install flask flask-sqlalchemy flask-restful
```

2. Initialize the database:
```bash
python create_db.py
```

3. Run the application:
```bash
python api.py
```

The server will start on `http://localhost:5000`
