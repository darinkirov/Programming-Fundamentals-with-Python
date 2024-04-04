def faro_shuffle(cards, shuffles):
    deck = cards.split()
    for _ in range(shuffles):
        half = len(deck) // 2
        shuffled_deck = []
        for i in range(half):
            shuffled_deck.append(deck[i])
            shuffled_deck.append(deck[i + half])
        deck = shuffled_deck
    return ' '.join(deck)

cards = input()
shuffles = int(input())
shuffled_cards = faro_shuffle(cards, shuffles)
print(shuffled_cards)
