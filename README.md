# CSE_210_01
 This is the Hilo card game. It is the week 1 assignment for programming with classes.

 directory:
 <root>
     deck.py
     hilo.py
 
  hilo.py:
     This is the main() file, so run it to play the game. It consists of a game loop, and a function to decide if the player wins or loses the round. The game will prompt the        user to enter if the next card will be of greater or lower value than a card shown on screen. If it is greater, the user gains 100 points, if it is lower, the user loses 75      points. The user always loses ties. The user starts with 300 points. The game ends when the user reaches 0 points or the deck runs out of cards.
 
 deck.py:
     A generalized module for working with decks. It has various functions such as generating, shuffling, and interpreting cards in a deck. Here are the functions:
     String [] get_deck():
         """Returns a deck of 52 cards, with one of each card type.
         They are organized with all the hearts first, (Ace-King),
         clubs second, diamonds third, and spades last.
         This deck does not include jokers or any other special cards.
         ♥ ♣ ♦ ♠
         """
     String [] shuffle_deck(String [] my_deck):
         """This will randomize the order of the elements in a 
         given list and return the list.
         """
     String get_suit(String card):
         """When given a string in the format of 'X of Y',
         will return Y. For example 'King of Diamonds' will
         return Diamonds.
         """
     String get_value_name(String card):
         """When given a string in the format of X of Y,
         will return X. For example 'King of Diamonds' will
         return King.
         """
     int get_value_number(String card):
         """Returns a number value for each of the cards.
         Ace is worth 1 by default, Jack is worth 11, Queen is worth 12,
         King is worth 13. The value of ace can be changed by specifying
         ace_value. Will throw an error if the input string is formatted
         incorerctly.
         """

