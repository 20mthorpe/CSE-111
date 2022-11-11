def add_team_end(new_team_end):
    basketball_teams.append(new_team_end)

def add_team(team_index, new_team):
    basketball_teams.insert(team_index, new_team)

def remove_team(remove_index):
    basketball_teams.pop(remove_index)

basketball_teams = []

i = 0


while i <= 5:
    new_team_end = input("What team will you add to the end of the list? ")
    add_team_end(new_team_end)

    new_team = input("What is the new team? ")
    team_index = int(input("Where in the list do you want it? "))
    add_team(team_index, new_team)

    remove_index = int(input("What item do you want to remove?(give the index) "))
    remove_team(remove_index)

    i += 1

print(f"This is the final list {basketball_teams}")
