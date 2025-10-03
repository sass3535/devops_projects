#How would each of the below be solved? 
#Suit spade, club, diamond, heart
#ace, king, queen, jack, 10-2
#card_count = 52
#2 players (dealer and player)
#player who gets 21 or greater than the other wins
#random number generator to shuffle deck and deal cards
#How would you deal the cards? How would the be displayed on the terminal?
#How would you determine winners?
#Aces are scored as 1 or 11

#Define card ranks and suits
# ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
# suits = ["♠️","♣️","♦️","❤️"]

# for i in ranks:
#     for x in suits:
#         cards = {i:x}   
#         print(cards)
#         print(help(cards))


def deck():
    cards  = {
        "♠️":["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"],
        "♣️":["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"],
        "♦️":["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"],
        "❤️":["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        }
    print(cards[1])