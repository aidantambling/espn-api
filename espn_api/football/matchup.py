from .team import Team

class Matchup(object):
    '''Creates Matchup instance'''
    def __init__(self, data):
        self.matchup_type = data.get('playoffTierType', 'NONE')
        self.week = data.get('matchupPeriodId')
        self.is_playoff = self.matchup_type != 'NONE'
        (self._home_team_id, self.home_score) = self._fetch_matchup_info(data, 'home')
        (self._away_team_id, self.away_score) = self._fetch_matchup_info(data, 'away')
        self.home_team: Team | None = None
        self.away_team: Team | None = None

    def __repr__(self):
        home = self.home_team if self.home_team is not None else self._home_team_id
        away = self.away_team if self.away_team is not None else self._away_team_id

        if self.week is not None:
            return f"Matchup(week={self.week}, home={home}, away={away})"
        return f"Matchup(home={home}, away={away})"

    def _fetch_matchup_info(self, data, team):
        '''Fetch info for matchup'''
        if team not in data:
            return (0, 0)
        team_id = data[team]['teamId']
        team_score = data[team]['totalPoints']

        return (team_id, team_score)
