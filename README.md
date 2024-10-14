# Tersea Demo FastAPI Application

This is a FastAPI application that provides a simple CRUD (Create, Read, Update, Delete) interface for managing books. The application uses MongoDB as the database and is containerized using Docker.

## Features

- List all books
- Get a specific book by ID
- Add a new book
- Update an existing book by ID
- Delete a book by ID

## Prerequisites

- Python 3.7 or higher
- Docker
- Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jutoken/fastapi-mongodb-docker-book-crud.git
   ```

2. Build and run the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This command will start both the FastAPI application and the MongoDB database.

## API Endpoints

### 1. List all books

- **Endpoint:** `GET /books/`
- **Response:** List of books

### 2. Get a specific book by ID

- **Endpoint:** `GET /books/{id}`
- **Parameters:** 
  - `id`: The ID of the book (string)
- **Response:** The book object
- **Error Response:** 404 if the book does not exist

### 3. Add a new book

- **Endpoint:** `POST /books/`
- **Body:** JSON object representing the book
- **Response:** The created book object

### 4. Update an existing book

- **Endpoint:** `PUT /books/{id}`
- **Parameters:**
  - `id`: The ID of the book (string)
- **Body:** JSON object with the updated book details
- **Response:** The updated book object
- **Error Response:** 400 if the update fails

### 5. Delete a book

- **Endpoint:** `DELETE /books/{id}`
- **Parameters:**
  - `id`: The ID of the book (string)
- **Response:** Success message
- **Error Response:** 400 if the delete fails

## Docker Compose Configuration

Here is the `docker-compose.yml` file used to configure the application and MongoDB:

```yaml
version: '3.8'
services:
  app:
    container_name: "tersea-group"
    build:
      dockerfile: ./Dockerfile
    ports:
      - 8080:8080
    depends_on:
      - db
    volumes:
      - .:/core
  db:
    image: mongo
    ports:
      - 27017:27017
```

## Running the Application

After starting the Docker containers, you can access the FastAPI application at:

```
http://localhost:8080
```

You can also view the automatically generated API documentation at:

```
http://localhost:8080/docs
```

