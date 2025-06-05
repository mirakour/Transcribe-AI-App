# Transcribe-AI Backend

A Flask-based backend service that stores audio transcriptions and AI-generated summaries. Enhanced with secure JWT-based authentication.

## Features

- Store and manage transcription metadata
- Attach summaries to transcription records
- Secure authentication using JWT tokens
- Password hashing using bcrypt
- PostgreSQL database integration
- CRUD operations for transcriptions and summaries

## Tech Stack

- Python (Flask)
- PostgreSQL
- SQLAlchemy (raw SQL queries)
- bcrypt (password hashing)
- PyJWT (token-based auth)
- Render (deployment)
- Postman (API testing)

---

## API Endpoints

### Auth

| Method | Route              | Description                 |
|--------|--------------------|-----------------------------|
| POST   | `/auth/register`   | Register a new user         |
| POST   | `/auth/login`      | Login and receive a token   |

### Transcriptions

| Method | Route                     | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/transcriptions/`        | Fetch all transcriptions        |
| POST   | `/transcriptions/`        | Add a new transcription         |
| GET    | `/transcriptions/<id>`    | Fetch single transcription      |
| PUT    | `/transcriptions/<id>`    | Update transcription details    |
| DELETE | `/transcriptions/<id>`    | Delete a transcription          |

### Summaries

| Method | Route               | Description                     |
|--------|---------------------|---------------------------------|
| GET    | `/summaries/`       | Fetch all summaries             |
| POST   | `/summaries/`       | Add a new summary               |
| GET    | `/summaries/protected` | 🔐 Protected test route      |

---

## Auth Flow

1. **Register**
   - `POST /auth/register`
   - Body:
     ```json
     {
       "username": "demo",
       "password": "123456"
     }
     ```

2. **Login**
   - `POST /auth/login`
   - Response:
     ```json
     {
       "token": "eyJhbGciOi..."
     }
     ```

3. **Access Protected Route**
   - `GET /summaries/protected`
   - Add header:
     ```
     Authorization: Bearer <your_token>
     ```

---

## Local Development

1. Clone the repo  
   ```bash
   git clone https://github.com/mirakour/Transcribe-AI-App.git
   cd Transcribe-AI-App