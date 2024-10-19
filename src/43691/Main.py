# 43691

player_atk = input()
player_def = input()
cache = ""
history = set()

while player_atk and player_def:
    # Check if there is a loop where no one can win
    id = f"{player_atk} {player_def}"
    if id in history:
        print(-1)
        exit(0)
    history.add(id)

    # Play a card out
    card = player_atk[0]
    player_atk = player_atk[1:]
    cache = card + cache

    # Check if any card is retrievable
    try:
        found_idx = cache.index(card, 1)
        player_atk += cache[:found_idx + 1]
        cache = cache[found_idx + 1:]
    except ValueError:
        # Swap two players
        player_atk, player_def = player_def, player_atk

print(player_atk)
