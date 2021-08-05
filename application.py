import constants
from copy import deepcopy

players_data = deepcopy(constants.PLAYERS)
teams_data = deepcopy(constants.TEAMS)

def clean_data():
  for player in players_data:
    if player["experience"] == "YES":
      player["experience"] = True
    else:
      player["experience"] = False
    player["height"] = int(player["height"][:2])


def balance_teams():
  Panthers = []
  Bandits = []
  Warriors = []
  teams = [Panthers, Bandits, Warriors]
  num_players_team = len(players_data) / len(teams)
  for player in range(len(players_data)):
    teams[player % num_players_team].append(players_data[player])
  return Panthers, Bandits, Warriors
  print (Panthers)


if __name__ == "__main__":
  clean_data()
  balance_teams()
#  test = balance_teams()
#  print(test)

#print ("PRESTON BASKETBALL TEAM STATS TOOL"'\n' 
#       "\n--- MENU ---" '\n'  
#       "\nHere are your choices:" 
#       "\nA.) Display Team Stats" 
#       "\nB.) Quit Application"
#       "\n"
#      )
#
#
#while True:
#  user_option = input("Enter an option: ").lower()  
#  if user_option == 'a':
#    print ("A.) Panthers" "\nB.) Bandits" "\nC.) Warriors")
#    break;
#  elif user_option == 'b':
#    print ("Thanks for stopping by for your sports fix today")
#    break;
#  else:
#    print ("I made this simple for you, pick one of the two options please")
#
#team_user_option = input("\nWhich team would you like to get data on?: ").lower()
#if team_user_option == 'a':
#  print ("\nTeam Panthers Stats"
#         "\n--------------------"
#         "\nTotal Players: ", len(Panthers))
#  print ("Players on Team: ")
#  
#print(type(Panthers))
#print(Panthers)
#
#for items in Panthers:
#  print(Panthers[item])