def count_remaining_players(cards):
    team_a_players = set(range(1, 12))
    team_b_players = set(range(1, 12))

    for card in cards:
        team, player = card.split('-')
        player = int(player)

        if team == 'A':
            if player in team_a_players:
                team_a_players.remove(player)
        elif team == 'B':
            if player in team_b_players:
                team_b_players.remove(player)

        if len(team_a_players) < 7 or len(team_b_players) < 7:
            print("Game was terminated")
            break

    print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")

# Taking input for the sequence of cards
cards_input = input("Enter the sequence of cards separated by a single space: ")

# Splitting the input sequence of cards
cards = cards_input.split()

# Counting remaining players on each team
count_remaining_players(cards)
