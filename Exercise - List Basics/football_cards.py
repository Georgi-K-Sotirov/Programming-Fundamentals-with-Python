team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
removed_players = []
red_card_players = input().split()
game_break = False
for current_player in red_card_players:
    current_player_list = current_player.split("-")
    current_player_team = current_player_list[0]
    if current_player in removed_players:
        continue
    removed_players.append(current_player)
    if current_player_team == "A":
        team_a.remove(current_player)
    elif current_player_team == "B":
        team_b.remove(current_player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_break = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_break:
    print("Game was terminated")