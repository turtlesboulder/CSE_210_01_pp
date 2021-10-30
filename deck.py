from random import randint

def shuffle_deck(my_deck:list):
    """This will randomize the order of the elements in a 
    given list and return the list.
    """
    new_deck = []
    for _ in range(len(my_deck)):
        index = randint(0,len(my_deck)-1)
        card = my_deck.pop(index)
        new_deck.append(card)

    return new_deck

def get_deck():
    """Returns a deck of 52 cards, with one of each card type.
    They are organized with all the hearts first, (Ace-King),
    clubs second, diamonds third, and spades last.
    This deck does not include jokers or any other special cards.
     ♥ ♣ ♦ ♠
    """
    my_deck = []
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    for suit in suits:
        for value in values:
            my_deck.append(f"{value} of {suit}")

    return my_deck

def get_suit(card:str):
    """When given a string in the format of X of Y,
    will return Y. For example 'King of Diamonds' will
    return Diamonds.
    """
    card_parts = card.split("of")
    return card_parts[1].strip()

def get_value_name(card:str):
    """When given a string in the format of X of Y,
    will return X. For example 'King of Diamonds' will
    return King.
    """
    card_parts = card.split("of")
    return card_parts[0].strip()

def get_value_number(card:str, ace_value = 1):
    """Returns a number value for each of the cards.
    Ace is worth 1 by default, Jack is worth 11, Queen is worth 12,
    King is worth 13. The value of ace can be changed by specifying
    ace_value. Will throw an error if the input string is formatted
    incorerctly.
    """
    card_parts = card.split("of")
    value = card_parts[0].strip()
    new_value = -1

    if value == "Ace":
        new_value = ace_value
    elif value == "Jack":
        new_value = 11
    elif value == "Queen":
        new_value = 12
    elif value == "King":
        new_value = 13
    else:
        new_value = int(value)

    return new_value
