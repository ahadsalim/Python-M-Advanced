import random
class human :
    def __init__(self,name) :
        self.name=name


class Footballer(human) :
    def __init__(self, name,team):
        super().__init__(name)
        self.team = team

player_names = ["Messi", "Ronaldo", "Neymar", "Salah", "Mbappe", "Hazard", "Van Dijk",
                "De Bruyne", "Lewandowski", "Mane", "Alisson", "Kante", "Ter Stegen",
                "Benzema", "Koulibaly", "Courtois", "Firmino", "Aguero", "Silva",
                "Sterling", "Griezmann", "Pogba"]

team_a=[]
team_b=[]

random.shuffle(player_names)
team_a = [Footballer(name, "Team A") for name in player_names[:11]]
team_b = [Footballer(name, "Team B") for name in player_names[11:]]

all_players = team_a + team_b

for player in all_players:
    print(f"{player.name} is in {player.team}")