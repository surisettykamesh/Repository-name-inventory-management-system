import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# MySQL Database URL
DATABASE_URL = os.getenv("DATABASE_URL")