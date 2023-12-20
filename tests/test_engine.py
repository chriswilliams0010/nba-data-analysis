# test_engine.py
import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from app.database.engine import (
    engine,
)  # Adjust the import path based on your project structure


def test_engine_connection():
    try:
        # Attempt to connect to the database
        with engine.connect() as conn:
            # Use SQLAlchemy's text() to ensure the query is correctly formatted
            query = text("SELECT version();")
            result = conn.execute(query)
            version_info = result.fetchone()
            assert (
                version_info is not None
            ), "Failed to fetch version info from database."
    except SQLAlchemyError as e:
        pytest.fail(f"Database connection failed: {e}")
