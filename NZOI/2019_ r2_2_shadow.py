player_count = int(input())
players = [None] * 101
dead = 0

max_pos = 0

for i in range(player_count):
    position, damage = input().split()
    position = int(position) + 1
    if position > max_pos:
        max_pos = position

    damage = int(damage)

    player_info = {"type": "player", "damage": damage, "health": 10, "alive": True}
    players[position] = player_info

shadow_position, shadow_damage = input().split()
shadow_position = int(shadow_position) + 1
shadow_damage = int(shadow_damage)
SHADOW_HEALTH = 60


while SHADOW_HEALTH > 0 and dead < player_count:
    total_dmg = 0

    closest_lower = max_pos
    closest_higher = max_pos
    for i, player in enumerate(players):
        if player:
            if player["alive"] == True:
                if shadow_position - i < closest_lower and shadow_position - i > 0:
                    closest_lower = i + 1
                elif i - shadow_position < closest_higher and i - shadow_position > 0:
                    closest_higher = i + 1

    print(f"{closest_higher=}")
    print(f"{closest_lower=}")
    print(f"{max_pos=}")

    players[closest_higher]["health"] -= shadow_damage
    players[closest_lower]["health"] -= shadow_damage

    if players[closest_higher]["health"] <= 0:
        dead += 1
        players[closest_higher]["alive"] = False

    if players[closest_lower]["health"] <= 0:
        dead += 1
        players[closest_lower]["alive"] = False

    for player in players:
        if player is not None:
            if player["alive"] == True:
                total_dmg += player["damage"]

    SHADOW_HEALTH -= total_dmg

    print(f"{SHADOW_HEALTH=}")
    print(f"{players=}")

if SHADOW_HEALTH < 0:
    living_players = []
    for i, player in enumerate(players):
        if player:
            if player["health"] > 0:
                living_players.append(str(i))

    print(f"We win! Players alive: {' '.join(living_players)}")
else:
    print("Shadow wins!")
