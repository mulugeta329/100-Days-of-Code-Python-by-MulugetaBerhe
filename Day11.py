import random
import os

def clear_terminal():
    """Clears the console screen across different platforms."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from a standard deck configuration."""
    # 11 represents the Ace. 10s represent Jack, Queen, King.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards_list):
    """Takes a list of cards and returns the total score calculated from them."""
    # Check for a natural Blackjack (2 cards totaling 21)
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0 # 0 will act as our internal signal for a natural Blackjack

    # Dynamic Ace Adjustment: If score is over 21 and contains an Ace (11), change it to 1
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
        
    return sum(cards_list)

def compare_scores(user_score, dealer_score):
    """Compares user vs dealer scores and returns the win/loss status message."""
    if user_score == dealer_score:
        return "👔 It's a draw/push!"
    elif dealer_score == 0:
        return "💀 Lose, dealer has a natural Blackjack!"
    elif user_score == 0:
        return "🏆 Win with a natural Blackjack!"
    elif user_score > 21:
        return "💥 You went over 21. You bust!"
    elif dealer_score > 21:
        return "💥 Dealer went over 21. Dealer busts! You win!"
    elif user_score > dealer_score:
        return "🎉 You have the higher score! You win!"
    else:
        return "📉 Dealer has the higher score. You lose."

def play_game():
    """Executes a single structural round of Blackjack."""
    print("==================================================")
    print("          ENTERPRISE BLACKJACK ENGINE v1.0        ")
    print("==================================================")

    user_cards = []
    dealer_cards = []
    is_game_over = False

    # Deal initial two-card hand to both positions
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # --- USER TURN ENGINE ---
    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's first card: [{dealer_cards[0]}]")

        # End turn early if someone hits blackjack or user busts
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("👉 Type 'y' to get another card, 'n' to pass: ").lower().strip()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            elif user_should_deal == 'n':
                is_game_over = True
            else:
                print("⚠️ Invalid entry. Standing with current hand.")
                is_game_over = True

    # --- DEALER TURN ENGINE ---
    # Dealer must hit continuously until their total score reaches 17 or higher
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    # --- FINAL SCOREBOARD ANALYSIS ---
    print("\n==================================================")
    print("                   FINAL RESULTS                  ")
    print("==================================================")
    print(f" 👤 Your final hand: {user_cards}, final score: {user_score if user_score != 0 else 21}")
    print(f" 🤖 Dealer's final hand: {dealer_cards}, final score: {dealer_score if dealer_score != 0 else 21}")
    print("--------------------------------------------------")
    print(compare_scores(user_score, dealer_score))
    print("==================================================\n")

# --- CORE APP RUNTIME LOOP ---
while input("🃏 Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower().strip() == "yes":
    clear_terminal()
    play_game()

print("\nThank you for utilizing the Blackjack Engine. System signing off.")