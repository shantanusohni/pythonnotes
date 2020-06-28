class Team(object):

    def __init__(self, team_name, *players):
        self.name = team_name
        self.players = players

    def __str__(self):
        return self.name

    def __gt__(self, other):
        if self.players > other.players:
            return True
        else:
            return False

    def __add__(self, other):
        return (self.players + other.players)
        """
        all_players = str()
        for player in self.players:
            all_players += ' ' + player
        for player in other.players:
            all_players += ' ' + player
        return all_players
        """


india = Team('India', 'Dhoni', 'Kohli', 'Amit', 'Nehra')
australia = Team('Australia', 'Smith', 'Lee', 'Haiden', 'warner')

print(len(australia))

