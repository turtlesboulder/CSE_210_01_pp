from random import randint
from deck import get_deck, shuffle_deck, get_value_number

"""
"""
def main():
    # Generate a deck from the deck module.
    my_deck = get_deck()
    # Shuffle the generated deck.
    my_deck = shuffle_deck(my_deck)
    first_card = my_deck.pop(0)
    print(game_loop(my_deck, first_card))

def game_loop(my_deck:list, first_card:str, points = 300):
    """This is the main loop the game will run in, it will check how many points
    the user has if the deck is empty. If it is not, it will let the user play the
    round and ask them if they want to play again.
    """
    if points > 0 and len(my_deck) > 0:
        user_input = input(
            f"The card is the {first_card}.\n Will the next one be higher or lower? [h/l]\n>> ")
        # This gets the next card in the deck, and removes it. This way we work through
        # the deck.
        next_card = my_deck.pop(0)
        passed = get_pass_fail(get_value_number(first_card),get_value_number(next_card), user_input)     
        if passed:
            points += 100
            print(f"The next card was the {next_card}! You win 100 points.")
            print(f"You have {points} points.")
        else:
            points -= 75
            print(f"The next card was the {next_card}. You lose 75 points.")
            print(f"You have {points} points.")

    if points <= 0:
        return "You are out of points! Thank you for playing."
    if len(my_deck) <= 0:
        return "The deck is out of cards! Thank you for playing."

    play_again = input("Do you want to play again? [y/n]\n>> ")
    if play_again == "y":
        return game_loop(my_deck, next_card, points)
    else:
        return "Thank you for playing!"


def get_pass_fail(num1, num2, guess):
    """This will compare two numbers against a guess
    as to which one is higher. If the guess is correct,
    this will return True.
    """
    passed = False
    if num1 < num2:
        if guess == "h":
            passed = True
    else:
        if num1 > num2 and guess == "l":
            passed = True
    return passed

if __name__ == "__main__":
    main()