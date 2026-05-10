import random

# Define the deck and suits
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Create the game state
columns = [[] for _ in range(10)]
foundation_piles = [[] for _ in range(8)]

# Deal the cards
for i in range(10):
    for j in range(5):
        columns[i].append(deck.pop())

# Flip the top card in each column
for column in columns:
    column[0] = (column[0][0], column[0][1], True)  # (rank, suit, face_up)

# Game loop
while True:
    # Print the game state
    print("Columns:")
    for i, column in enumerate(columns):
        print(f"{i+1}: {', '.join([f'{card[0]} of {card[1]}' for card in column if card[2]])}")
    print("Foundation Piles:")
    for i, pile in enumerate(foundation_piles):
        print(f"{i+1}: {', '.join([f'{card[0]} of {card[1]}' for card in pile])}")

    # Get user input
    command = input("Enter a command (e.g. 'move 1 2' to move a card from column 1 to column 2): ")

    # Parse the command
    parts = command.split()
    if parts[0] == 'move':
        from_column = int(parts[1]) - 1
        to_column = int(parts[2]) - 1
        card = columns[from_column].pop()
        columns[to_column].append(card)
    elif parts[0] == 'foundation':
        column = int(parts[1]) - 1
        card = columns[column].pop()
        foundation_piles[card[1]].append(card)
    else:
        print("Invalid command. Try again!")

    # Check for win condition
    if all(len(pile) == 13 for pile in foundation_piles):
        print("Congratulations, you won!")
        break