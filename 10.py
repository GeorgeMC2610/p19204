import random

def whatIsMyHand(hand):
    card_numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    card_types   = ["Diamonds", "Spades", "Hearts", "Clubs"]

    straight    = (hand[0][0] == (hand[1][0] - 1)) and (hand[1][0] == (hand[2][0] - 1)) and (hand[2][0] == (hand[3][0] - 1)) and (hand[3][0] == (hand[4][0] - 1))
    flush       = (hand[0][1] == hand[1][1]) and (hand[1][1] == hand[2][1]) and (hand[2][1] == hand[3][1]) and (hand[3][1] == hand[4][1]) and (hand[4][1] == hand[0][1])
    royal_flush = (flush) and (straight) and (hand[0][0] == 10)

    #Ορισμός του χεριού Royal Flush (δηλαδή πέντε χαρτιά ίδιου τύπου σε σειρά, ξεκινώντας από το 10 και φτάνοντας στον άσσο)
    if royal_flush:
        return "Royal Flush"

    #Χέρι 'Straight Flush' (χαρτιά σε σειρά με ίδιο τύπο)
    if (flush) and (straight):
        return "Straight Flush"

    #Ορισμός του χεριού FLUSH (Πέντε ίδιοι τύποι)
    if flush:
        return "Flush"
    
    #Ορισμός του χεριού STRAIGHT (Χαρτιά σε σειρά)
    if straight:
        return "Straight"

    

#Ορισμός των καρτών
card_numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
card_types   = ["Diamonds", "Spades", "Hearts", "Clubs"]
cards        = []

for number in card_numbers:
    for Type in card_types:
        card_pair = (number, Type)
        cards.append(card_pair)

#Ανακάτεμα καρτών
random.shuffle(cards)

player1_cards = []
player2_cards = []

for i in range(0,5):
    player1_cards += [cards.pop()]
    player2_cards += [cards.pop()]

player1_cards.sort()
player2_cards.sort()

#player1_cards = [(10, 'Clubs'), (11, 'Clubs'), (12, 'Clubs'), (13, 'Clubs'), (14, 'Clubs')]

print(whatIsMyHand(player1_cards))

print("Player 1 Cards:", player1_cards)
print("Player 2 Cards:", player2_cards)