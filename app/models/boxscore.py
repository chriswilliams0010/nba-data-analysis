import logging
from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

logger = logging.getLogger(__name__)
Base = declarative_base()


class Boxscore(Base):
    """
    Represents a boxscore for a specific game in the NBA.

    Attributes:
        boxscore_id (int): The unique identifier for a specific boxscore.
        schedule_id (int): Secondary key for the schedule associated with the boxscore.
        team_id (int): Secondary key for the team of the player associated with the boxscore.
        player_id (int): Secondary key for the player associated with the boxscore.
        starter (bool): Boolean indicating whether or not the player associated was a starter.
        min_played (int): Number of minutes played.
        field_goal (int): Number of field goals made.
        fg_attempt (int): Number of field goals attempted.
        fg_per (int): Field goal percentage (field_goal/fg_attempt)
        three_point (int): Number of 3pt field goals made.
        tp_attempt (int): Number of 3pt field goals attempted.
        tp_per (int): 3pt percentage (three_point/tp_attempt).
        free_throw (int): Number of free throws made.
        ft_attempt (int): Number of free throws attempted.
        ft_per (int): Free throw percentage (free_throw/ft_attempt).
        off_rebounds (int): Number of offensive rebounds.
        def_rebounds (int): Number of defensive rebounds.
        tot_rebounds (int): Number of total rebounds.
        assists (int): Number of assists.
        steals (int): Number of steals.
        blocks (int): Number of blocks.
        turnovers (int): Number of turnovers.
        personal_fouls (int): Number of personal fouls.
        points (int): Number of points scored.
        plus_minus (int): Estimates players contribution to the team when that player is on the court.
        true_shoot_per (int): True shooting percentage of the player.
        effective_fg_per (int): Effective field goal percentage of the player.
        tpa_rate (int): Three point attempt rate of player.
        ft_rate (int): Free throw rate of player.
        off_reb_per (int): Offensive rebound percentage of player.
        def_reb_per (int): Defensive rebound percentage of player.
        tot_reb_per (int): Total rebound percentage of player.
        ast_per (int): Assist percentage.
        stl_per (int): Steal percentage.
        blk_per (int): Block percentage.
        tov_per (int): Turnover percentage.
        usage_per (int): Usage percentage.
        off_rating (int): Offensive rating.
        def_rating (int): Defensive rating.
        box_plus_minus (int): Boxscore plus/minus rating.
    """

    __tablename__ = "boxscores"

    boxscore_id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, ForeignKey("schedules.schedule_id"))
    team_id = Column(Integer, ForeignKey("teams.team_id"))
    player_id = Column(Integer, ForeignKey("players.player_id"))
    starter = Column(Boolean)
    min_played = Column(Integer)
    field_goal = Column(Integer)
    fg_attempt = Column(Integer)
    fg_per = Column(Integer)
    three_point = Column(Integer)
    tp_attempt = Column(Integer)
    tp_per = Column(Integer)
    free_throw = Column(Integer)
    ft_attempt = Column(Integer)
    ft_per = Column(Integer)
    off_rebounds = Column(Integer)
    def_rebounds = Column(Integer)
    tot_rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personal_fouls = Column(Integer)
    points = Column(Integer)
    plus_minus = Column(Integer)
    true_shoot_per = Column(Integer)
    effective_fg_per = Column(Integer)
    tpa_rate = Column(Integer)
    ft_rate = Column(Integer)
    off_reb_per = Column(Integer)
    def_reb_per = Column(Integer)
    tot_reb_per = Column(Integer)
    ast_per = Column(Integer)
    stl_per = Column(Integer)
    blk_per = Column(Integer)
    tov_per = Column(Integer)
    usage_per = Column(Integer)
    off_rating = Column(Integer)
    def_rating = Column(Integer)
    box_plus_minus = Column(Integer)

    schedule = relationship("Schedule")
    team = relationship("Team")
    player = relationship("Player")


    def __repr__(self):
        return (
            f"<Boxscore("
            f"boxscore_id={self.boxscore_id}, "
            f"schedule_id={self.schedule_id}, "
            f"team_id={self.team_id}, "
            f"player_id={self.player_id}, "
            f"starter={self.starter}, "
            f"min_played={self.min_played}, "
            f"field_goal={self.field_goal}, "
            f"fg_attempt={self.fg_attempt}, "
            f"fg_per={self.fg_per}, "
            f"three_point={self.three_point}, "
            f"tp_attempt={self.tp_attempt}, "
            f"tp_per={self.tp_per}, "
            f"free_throw={self.free_throw}, "
            f"ft_attempt={self.ft_attempt}, "
            f"ft_per={self.ft_per}, "
            f"off_rebounds={self.off_rebounds}, "
            f"def_rebounds={self.def_rebounds}, "
            f"tot_rebounds={self.tot_rebounds}, "
            f"assists={self.assists}, "
            f"steals={self.steals}, "
            f"blocks={self.blocks}, "
            f"turnovers={self.turnovers}, "
            f"personal_fouls={self.personal_fouls}, "
            f"points={self.points}, "
            f"plus_minus={self.plus_minus}, "
            f"true_shoot_per={self.true_shoot_per}, "
            f"effective_fg_per={self.effective_fg_per}, "
            f"tpa_rate={self.tpa_rate}, "
            f"ft_rate={self.ft_rate}, "
            f"off_reb_per={self.off_reb_per}, "
            f"def_reb_per={self.def_reb_per}, "
            f"tot_reb_per={self.tot_reb_per}, "
            f"ast_per={self.ast_per}, "
            f"stl_per={self.stl_per}, "
            f"blk_per={self.blk_per}, "
            f"tov_per={self.tov_per}, "
            f"usage_per={self.usage_per}, "
            f"off_rating={self.off_rating}, "
            f"def_rating={self.def_rating}, "
            f"box_plus_minus={self.box_plus_minus}"
            f")>"
        )
