import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()

class Team(Base):
    """
    Represents a team in the NBA.

    Attributes:
        team_id (int): The unique identifier for the team.
        team_name (str): The name of the team.
    """
    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(255), nullable=False)
    team_acronym = Column(String(3), nullable=False)

    def __repr__(self):
        return f"<Team(team_id={self.team_id}, team_name='{self.team_name}')>"
