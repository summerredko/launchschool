import random

# Initiate the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# Shuffle the cards
def shuffle(deck):
    random.shuffle(deck)

# Message user
def prompt(message):
    print(f'==> {message}')

# Calculate the value of hand
def calculate_hand_value(cards):
    value = 0
    ace_count = 0

    for card in cards:
        rank = card.split()[0]  

        if rank in ['Jack', 'Queen', 'King']: 
            value += 10
        elif rank == 'Ace':  
            value += 11
            ace_count += 1
        else:  
            value += int(rank)

    # Adjust for Aces if value exceeds 21
    while value > 21 and ace_count:
        value -= 10  
        ace_count -= 1

    return value

def busted(hand):
    return calculate_hand_value(hand) > 21

print()
prompt('Welcome to Twenty-One!')
print()
prompt("HOW TO PLAY:")
prompt("""Players aim to have a hand value as close """
        """to 21 as possible without exceeding it.""")
prompt("""Compete against the dealer.""")
print()

# Shuffle the deck
shuffle(deck)
while True:
    # Assign the cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Display initial hands
    prompt(f'Dealer has: {dealer_hand[0]} and unknown card')
    prompt(f'You have: {player_hand[0]} and {player_hand[1]}')

    # Tally scores
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    prompt(f"Your current hand value is: {player_score}")

    # Player turn
    while True:
        answer = input("Hit or stay? (h or s): ").strip().lower()
        if answer == 's':
            prompt("You chose to stay!")
            break
        elif answer == 'h':
            player_hand.append(deck.pop())
            player_score = calculate_hand_value(player_hand)
            prompt(f'You drew {player_hand[-1]}. Your current hand value is: {player_score}')
            if busted(player_hand):
                prompt('You busted! Dealer wins.')
                break
        else:
            prompt("Invalid choice. Please enter 'h' to hit or 's' to stay.")

    # Dealer turn
    if not busted(player_hand):
        prompt(f"Dealer's hand: {dealer_hand[0]} and {dealer_hand[1]}")
        while dealer_score < 17:
            dealer_hand.append(deck.pop())
            dealer_score = calculate_hand_value(dealer_hand)
            prompt(f'Dealer drew {dealer_hand[-1]}. Dealer hand value is: {dealer_score}')
            if busted(dealer_hand):
                prompt('Dealer busted! You win.')
                break

    # Compare hands if no one busted
    if not busted(player_hand) and not busted(dealer_hand):
        prompt(f"Dealer's final hand value is: {dealer_score}")
        prompt(f"Your final hand value is: {player_score}")
        if dealer_score > player_score:
            prompt('Dealer wins.')
        elif dealer_score < player_score:
            prompt('You win!')
        else:
            prompt("It's a tie!")

    # Ask to play again
    answer = input('Play again? (y or n): ').strip().lower()
    if answer == 'n':
        prompt('Thanks for playing Twenty-One!')
        break
