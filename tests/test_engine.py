import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from app.database.engine import engine


def test_engine_connection():
    try:
        with engine.connect() as conn:
            query = text("SELECT version();")
            result = conn.execute(query)
            version_info = result.fetchone()
            assert (
                version_info is not None
            ), "Failed to fetch version info from database."
    except SQLAlchemyError as e:
        pytest.fail(f"Database connection failed: {e}")
