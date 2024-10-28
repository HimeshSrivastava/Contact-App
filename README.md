# Flask CRUD Application for MongoDB(Contact-App)

This is a simple Flask application that provides a REST API for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource and manage the users in contact list.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Features

- Create a new user.
- Retrieve a list of all users or a specific user by ID.
- Update an existing user.
- Delete a user.
- Dockerized application for easy deployment.

## Requirements

- Python 3.x
- Flask
- PyMongo
- MongoDB (local or cloud instance)
- Docker (for containerization)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HimeshSrivastava/Contact-App.git
   cd "Contact-App"

2. **Set the MongoDB URI:**
   MONGO_URI=mongodb+srv://himeshsrivastava123:rk9RUCdC3aJsdqWA@cluster0.aqzjeb9.mongodb.net/Database_backend

3. **Build and run the Docker container:**   
   docker build -t flask-mongo-crud .
   docker run -p 5000:5000 flask-mongo-crud

4. **Access the application:**
   Open your browser and navigate to http://localhost:5000.

## API Endpoints

   Method	   Endpoint	           Description
   GET	     /api/users	          Get a list of all users
   GET	     /api/users/<id>      Get a user by ID
   POST	     /api/users	          Create a new user
   PUT	     /api/users/<id>	  Update a user by ID
   DELETE	 /api/users/<id>	  Delete a user by ID


## Testing

**You can test the API endpoints using Postman:**

   1. GET /api/users - Retrieves all users.
   2. GET /api/users/{id} - Retrieves a user by ID.
   3. POST /api/users - Creates a new user. Provide JSON data in the request body.
   4. PUT /api/users/{id} - Updates an existing user. Provide JSON data in the request body.
   5. DELETE /api/users/{id} - Deletes a user by ID.

## License

    This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
