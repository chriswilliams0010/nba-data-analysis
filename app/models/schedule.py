import logging
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

logger = logging.getLogger(__name__)
Base = declarative_base()


class Schedule(Base):
    """
    Represents a specific game in the NBA.

    Attributes:
        schedule_id (int): The unique identifier for a specific game.
        date (datetime): The date of the game.
        start_et (str): The start time of the game.
        home (int): Secondary key for the home team.
        pts_home (int): The number of points accumulated by the home team.
        away (int): Secondary key for the away team.
        pts_away (int): The number of points accumulated by the away team.
        ot (str): Column signifying overtimeand longer games.
        arena (int): Secondary key for the arena game was played.
        attendance (int): Number of people that attended the game.
        notes (str): Additional notes for the game.
        playoffs (bool): Boolean value for whether game was a playoff game.
        url (str): URL for boxscore for specific game.
    """

    __tablename__ = "schedules"

    schedule_id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    start_et = Column(String(10))
    home_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    pts_home = Column(Integer)
    away_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    pts_away = Column(Integer)
    ot = Column(String(4))
    arena_id = Column(Integer, ForeignKey("arenas.arena_id"))
    attendance = Column(Integer)
    notes = Column(String(255))
    playoffs = Column(Boolean)
    url = Column(String(150))

    home = relationship("Team")
    away = relationship("Team")
    arena = relationship("Arena")
    
    def __repr__(self):
        return (f"<Schedule(schedule_id={self.schedule_id}, "
                f"date={self.date}, "
                f"start_et='{self.start_et}', "
                f"home_id={self.home_id}, "
                f"pts_home={self.pts_home}, "
                f"away_id={self.away_id}, "
                f"pts_away={self.pts_away}, "
                f"ot='{self.ot}', "
                f"arena_id={self.arena_id}, "
                f"attendance={self.attendance}, "
                f"notes='{self.notes}', "
                f"playoffs={self.playoffs}, "
                f"url='{self.url}')>")
