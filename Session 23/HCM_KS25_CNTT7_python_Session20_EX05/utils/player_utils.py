def find_player(records, player_id):
    clean_id = player_id.strip().upper()
    for player in records:
        if player["player_id"] == clean_id:
            return player
    return None