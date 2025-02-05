import json

print('test interview script')

class Team():
    def __init__(self, team_name):
        self.name = team_name
        self.gp = 0
        self.w = 0
        self.d = 0
        self.l = 0
        self.points = 0 
        self.gs = 0
        self.ga = 0

    def add_result(self, gs, ga):
        self.gs += gs
        self.ga += ga
        self.gp += 1
        #draw
        if(gs == ga):
            self.d += 1
            self.points += 1

        #loss
        elif(gs < ga):
            self.l += 1

        #win 
        else:
            self.w +=1
            self.points+=3 



path = '22-23.json'

with open(path) as f:
    matches = json.load(f)
    

teams = {}

for match in matches:
    home_team = match['homeTeam']
    away_team = match['awayTeam']

    #check if teams are in teams otherwise add them 
    if home_team not in teams:
        teams[home_team] = Team(home_team)
    if away_team not in teams:
        teams[away_team] = Team(away_team)

    
    #increment the home 
    teams[home_team].add_result(match['homeGoals'], match['awayGoals'])

    #incremnt the teams 
    teams[away_team].add_result(match['awayGoals'], match['homeGoals'])
i = 0
for key in teams.keys():
    print(teams[key].gp)
    i+=1
    print(i)
unsorted_teams =  teams.values()
print(f'{"Name":<15} {"W":<3} {"D":<3} {"L":<3} {"GD":<5} {"Pts":<5}')
sorted_teams = sorted(unsorted_teams, key=lambda team: team.points, reverse=True)

for team in sorted_teams:
    print(f'{team.name:<15} {team.w:<3} {team.d:<3} {team.l:<3} {team.gs - team.ga:<5} {team.points:<5}')