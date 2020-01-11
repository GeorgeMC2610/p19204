import random

def whatIsMyHand(hand):
    card_numbers = [2,3,4,5,6,7,8,9,"A","J","Q","K"]
    card_types   = ["Diamonds", "Spades", "Hearts", "Clubs"]

    #Ορισμός του χεριού FIVE OF A KIND
    for card in hand:
        if card[i]:
            break

#Ορισμός των καρτών
card_numbers = [2,3,4,5,6,7,8,9,10,"A","J","Q","K"]
card_types   = ["Diamonds", "Spades", "Hearts", "Clubs"]
cards        = ["Joker", "Joker"]

for number in card_numbers:
    for Type in card_types:
        card_pair = [number, Type]
        cards.append(card_pair)

#Ανακάτεμα καρτών
random.shuffle(cards)

player1_cards = []
player2_cards = []

for i in range(0,5):
    player1_cards += [cards.pop()]
    player2_cards += [cards.pop()]

print("Player 1 Cards:", player1_cards)
print("Player 2 Cards:", player2_cards)