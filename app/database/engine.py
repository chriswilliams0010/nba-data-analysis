from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Database connection settings config in venv activate file
DB_USERNAME = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", "5432")  # Default PostgreSQL port is 5432
DB_NAME = os.environ.get("DB_NAME")

# Connection string for the database
# Format: dialect+driver://username:password@host:port/database
DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
