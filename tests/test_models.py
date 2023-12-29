from app.models.team import Team
from src.cities import cities


def test_team_creation():
    """Test the creation of a Team instance"""
    team_name = next(iter(cities))
    team_acronym = cities[team_name]
    team = Team(team_id=1, team_name=team_name, team_acronym=team_acronym)
    assert team.team_id == 1
    assert team.team_name == team_name
    assert team.team_acronym == team_acronym
