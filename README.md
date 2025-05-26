# 🚀 DockerHub Private Repository Manager

A FastAPI and PostgreSQL-based backend service for managing private DockerHub repositories.

## 📋 Overview

This service provides a robust solution for managing private DockerHub repositories by:
- Storing repository details (image name, tag, token) in PostgreSQL
- Providing RESTful API endpoints for repository management
- Enabling secure interaction with DockerHub repositories

## 🎯 Features

- Submit and store private DockerHub repository details
- Secure token management
- RESTful API endpoints for CRUD operations
- PostgreSQL database integration
- DockerHub API integration

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: DockerHub Tokens
- **API Documentation**: OpenAPI/Swagger

## 📡 API Endpoints

### Create Repository
```http
POST /repository
```

**Request Body:**
```json
{
  "image_name": "yourusername/private-image",
  "tag": "latest",
  "token": "your_dockerhub_token"
}
```

**Response:**
```json
{
  "status code": 201,
  "message": "Repository created successfully",
  "id": "d5a61bb0-4713-4b76-b1ad-15f9dbe9c823"
}
```

### List All Repositories
```http
GET /repository
```

**Response:**
```json
{
  "status code": 200,
  "message": "Repositories fetched successfully",
  "repositories": [
    {
      "id": "51619497-f405-45c4-9386-163d72d991e9",
      "image_name": "yourusername/my-private-image",
      "tag": "latest"
    }
  ]
}
```

### Get Repository by ID
```http
GET /repository/{repo_id}
```

**Response:**
```json
{
  "status code": 200,
  "message": "Repository fetched successfully",
  "repository": {
    "id": "51619497-f405-45c4-9386-163d72d991e9",
    "image_name": "yourusername/my-private-image",
    "tag": "latest"
  }
}
```

## 🗄️ Database Schema

### Table: `docker_repositories`

| Column     | Type   | Description                      |
|------------|--------|----------------------------------|
| id         | UUID   | Unique identifier (Primary Key)  |
| image_name | String | Docker image name                |
| tag        | String | Docker image tag                 |
| token      | String | DockerHub access token           |

## ⚙️ Configuration

Create a `.env` file in the `app/` directory with the following variables:

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=dockerdb
DB_USER=postgres
DB_PASSWORD=root
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!--
Problem Statement:
Build a backend service to:
- Accept private DockerHub repository details such as Docker image name, tag, and token from the user.
- Store this information in a PostgreSQL database.
- Interact with DockerHub APIs or Docker CLI commands to perform repository actions (e.g., pushing images).
- Expose FastAPI endpoints to manage and retrieve these records.
-->

## 🧩 Problem Statement

This project allows users to:

- Submit private DockerHub repository details (image name, tag, token).
- Store them in a PostgreSQL database.
- Retrieve and manage this data using FastAPI endpoints.

---

<!--
Expected Output:
1. A UI form (frontend in any JS framework) to accept DockerHub repository details.
2. A FastAPI POST endpoint to store the input and return a unique ID.
3. A GET endpoint to list all saved DockerHub repositories.
4. A GET endpoint to fetch details of a specific DockerHub repository by its ID.
5. Database schema to store repository details.
-->

## 🎯 Expected Output

- Frontend form for input (to be built separately).
- Three FastAPI endpoints:
  - `POST /repository` – Add a new entry.
  - `GET /repository` – List all entries.
  - `GET /repository/{id}` – Get a single entry.
- PostgreSQL schema to persist the repository info.

---

<!--
.env File:
Environment variables to connect to PostgreSQL DB.
-->

## 📁 Environment File (`.env`)

Place this `.env` file inside the `app/` directory:

<pre><code>DB_HOST=localhost
DB_PORT=5433
DB_NAME=dockerdb
DB_USER=postgres
DB_PASSWORD=root
</code></pre>

---

<!--
API Endpoints:
Describes available endpoints, payloads, and sample responses.
-->

## 📡 API Endpoints

```json
1. POST /repository
{
  "image_name": "yourusername/private-image",
  "tag": "latest",
  "token": "your_dockerhub_token"
}
Response:
{
  "status code": 201,
  "message": "Repository created successfully",
  "id": "d5a61bb0-4713-4b76-b1ad-15f9dbe9c823"
}

2. GET /repository
Response:
{
  "status code": 200,
  "message": "Repositories fetched successfully",
  "repositories": [
    {
      "id": "51619497-f405-45c4-9386-163d72d991e9",
      "image_name": "yourusername/my-private-image",
      "tag": "latest"
    }
  ]
}

3. GET /repository/{repo_id}
Response:
{
  "status code": 200,
  "message": "Repository fetched successfully",
  "repository": {
    "id": "51619497-f405-45c4-9386-163d72d991e9",
    "image_name": "yourusername/my-private-image",
    "tag": "latest"
  }
}
If not found:
{
  "status code": 404,
  "message": "Repository not found"
}

---

## 🗄️ Database Schema

Table design for `docker_repositories`:

| Column     | Type   | Description                      |
|------------|--------|---------------------------------|
| id         | UUID   | Unique identifier (Primary Key) |
| image_name | String | Docker image name               |
| tag        | String | Docker image tag                |
| token      | String | DockerHub access token          |

---

## 🛠️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload
