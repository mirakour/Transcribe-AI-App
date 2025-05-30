DROP TABLE IF EXISTS summaries;
DROP TABLE IF EXISTS transcriptions;

CREATE TABLE transcriptions (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    source_type TEXT NOT NULL,
    speaker_count INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE summaries (
    id SERIAL PRIMARY KEY,
    transcription_id INTEGER REFERENCES transcriptions(id) ON DELETE CASCADE,
    summary_text TEXT NOT NULL
);