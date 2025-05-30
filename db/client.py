import os
import psycopg2 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create a reusable DB connection function
def get_connection():
    return psycopg2.connect(DATABASE_URL)