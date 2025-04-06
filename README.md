# FastAPI Blog API

This is a simple FastAPI application for managing posts in a blog-like system. It includes features such as user authentication, CRUD operations for posts, and caching for retrieving posts efficiently.

## Features

- **User Authentication**: Users can sign up, log in, and access their posts.
- **Post Management**: Users can create, read, update, and delete their posts.
- **Caching**: Posts retrieval is cached for 5 minutes to improve performance.
- **Database**: Uses MySQL for persistent storage.
- **Environment Configuration**: Configurable via environment variables.

## Technologies Used

- FastAPI
- SQLAlchemy (ORM)
- MySQL
- Pydantic for data validation
- JWT for authentication
- Uvicorn (ASGI server)
- Python 3.x

## Requirements

To run the project, you will need:

- Python 3.x
- MySQL database
- Docker (optional for containerized environment)
