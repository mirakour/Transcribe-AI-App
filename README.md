## Transcribe AI [Backend]

A backend API for a web + mobile-based AI transcription service.
Built with Flask and PostgreSQL.

This backend will serve a mobile/web app that:
- Accepts audio/video uploads
- Stores transcription metadata
- Simulates transcription + speaker identification (mocked for now)
- Stores summaries

## Features

- Full CRUD API for `transcriptions` and `summaries`
- Each transcription can have one generated summary
- PostgreSQL database with relational schema
- RESTful endpoints
- Meaningful error handling and validations

---

## Database Schema

### `transcriptions`
| Field           | Type     | Notes                           |
|----------------|----------|----------------------------------|
| id             | SERIAL   | Primary Key                      |
| filename       | TEXT     | NOT NULL                         |
| source_type    | TEXT     | ("live", "upload", "zoom", etc.) |
| speaker_count  | INTEGER  | NOT NULL                         |
| created_at     | TIMESTAMP | Defaults to `NOW()`             |

### `summaries`
| Field           | Type     | Notes                       |
|----------------|----------|------------------------------|
| id             | SERIAL   | Primary Key                  |
| transcription_id | INTEGER | FK → transcriptions(id)     |
| summary_text   | TEXT     | NOT NULL                     |

---

## API Endpoints

### Transcriptions
| Method | Endpoint                    | Description                   |
|--------|-----------------------------|-------------------------------|
| GET    | `/transcriptions`           | Get all transcriptions        |
| GET    | `/transcriptions/<id>`      | Get a transcription by ID     |
| POST   | `/transcriptions`           | Create a transcription        |
| PUT    | `/transcriptions/<id>`      | Update a transcription        |
| DELETE | `/transcriptions/<id>`      | Delete a transcription        |

### Summaries
| Method | Endpoint        | Description                              |
|--------|-----------------|------------------------------------------|
| GET    | `/summaries`    | Get all summaries with filenames         |
| POST   | `/summaries`    | Create a summary (link to transcription) |

---

## How to Run Locally

### 1. Clone + Install

```bash
git clone https://github.com/mirakour/Transcribe-AI-App.git
cd transcribe_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
