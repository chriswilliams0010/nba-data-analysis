import logging
from sqlalchemy import Column, Integer, String, ARRAY, Boolean, DateTime
from sqlalchemy.orm import declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()


class Player(Base):
    """
    Represents a player in the NBA.

    Attributes:
        player_id (int): The unique identifier for the player.
        player_name (str): The name of the player.
        position (array(str)): The position of the player.
        height_in (int): Player's height in inches.
        weight (int): Player's weight in pounds.
        birth_date (datetime): Player's date of birth.
        hometown (str): Player's place of birth.
        college (str): College player attended.
        draft_year (int): Year player was drafted.
        draft_round (int): Round player was drafted.
        draft_pick (int): Number player was drafted.
        nba_debut_year (int): Year player debuted in the NBA.
        nba_final_year (int): Final year player played in the NBA.
    """

    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True)
    player_name = Column(String(255), nullable=False)
    position = Column(ARRAY(String))
    height_in = Column(Integer)
    weight = Column(Integer)
    birth_date = Column(DateTime)
    hometown = Column(String(255))
    college = Column(String(255))
    draft_year = Column(Integer)
    draft_round = Column(Integer)
    draft_pick = Column(Integer)
    nba_debut_year = Column(Integer)
    nba_final_year = Column(Integer)

    def __repr__(self):
        return f"<Player(player_id={self.player_id}, player_name='{self.player_name}', position='{self.position}', height_in={self.height_in}, weight={self.weight}, birth_date={self.birth_date}, hometown='{self.hometown}', college='{self.college}', draft_year={self.draft_year}, draft_round={self.draft_round}, draft_pick={self.draft_pick}, nba_debut_year={self.nba_debut_year}, nba_final_year={self.nba_final_year})>"
