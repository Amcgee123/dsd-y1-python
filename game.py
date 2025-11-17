games = ["Resident Evil (1)","Team Fortress 2 (2)","Hollow Knight (3)","Half-Life 2 (4)","Doom 2019 (5)","Arc Raiders (6)","Terraria (7)","Planet Coaster (8)","Portal 2 (9)","Undertale (10)"
]


game_status = {}

for game in games:
  
    played_input = input(f"Have you played {game}? (y/n): ").lower()
    played = played_input == "y"

    favorite_input = input(f"Is {game} a favorite? (y/n): ").lower()
    favorite = favorite_input == "y"

    game_status[game] = {"played": played, "favorite": favorite}

print("\n--- Game Summary ---")
for game, status in game_status.items():
    if status["played"]:
        played_text = "Played"
    else:
        played_text = "Not played"

    if status["favorite"]:
        favorite_text = "Favorite"
    else:
        favorite_text = "Not favorite"

    print(f"{game}: {played_text}, {favorite_text}")
