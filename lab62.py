class Team:
    name = "normal default Team"


team1 = Team()
team2 = Team()
print team1.name, team2.name
team1.name = "Mobile R&D"
print team1.name, team2.name
Team.name = "**Normal Team**"
print team1.name, team2.name
del team1.name
print team1.name, team2.name
team1.size = 7
team1.leader = 'John'
print team1.size, team1.leader, team1.name
