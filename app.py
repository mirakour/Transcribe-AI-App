from flask import Flask
from routes.transcriptions import transcriptions_bp
from routes.summaries import summaries_bp
from routes.auth import auth_bp  # make sure to only import once

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Transcribe-AI Flask Backend is running!"

# Register Blueprints
app.register_blueprint(transcriptions_bp, url_prefix='/transcriptions')
app.register_blueprint(summaries_bp, url_prefix='/summaries')
app.register_blueprint(auth_bp, url_prefix='/auth')