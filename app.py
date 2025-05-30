from flask import Flask
from routes.transcriptions import transcriptions_bp
from routes.summaries import summaries_bp

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Transcribe-AI Flask Backend is running!"

# Register Blueprints
app.register_blueprint(transcriptions_bp, url_prefix='/transcriptions')
app.register_blueprint(summaries_bp, url_prefix='/summaries')