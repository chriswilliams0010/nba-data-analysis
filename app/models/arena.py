import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()


class Arena(Base):
    """
    Represents an arena used by the NBA.

    Attributes:
        arena_id (int): The unique identifier for the player.
        arena_name (str): The name of the arena.
        arena_loc (str): The location of the arena.
    """

    __tablename__ = "arenas"

    arena_id = Column(Integer, primary_key=True)
    arena_name = Column(String(255), nullable=False)
    arena_loc = Column(String(255))

    def __repr__(self):
        return f"<Arena(arena_id={self.arena_id}, arena_name='{self.arena_name}', arena_loc='{self.arena_loc}')>"
    