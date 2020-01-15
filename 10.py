import random

def whatIsMyHand(hand):
    straight    = (hand[0][0] == (hand[1][0] - 1)) and (hand[1][0] == (hand[2][0] - 1)) and (hand[2][0] == (hand[3][0] - 1)) and (hand[3][0] == (hand[4][0] - 1))
    flush       = (hand[0][1] == hand[1][1]) and (hand[1][1] == hand[2][1]) and (hand[2][1] == hand[3][1]) and (hand[3][1] == hand[4][1]) and (hand[4][1] == hand[0][1])
    full_house  = ((hand[0][0] == hand[1][0]) and (hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0])) or ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0]) and (hand[3][0] == hand[4][0]))
    kind_4      = ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0])) or ((hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0]))
    kind_3      = ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0])) or ((hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0])) or ((hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0]))
    kind_2      = ((hand[0][0] == hand[1][0]) or (hand[1][0] == hand[2][0]) or (hand[2][0] == hand[3][0]) or (hand[3][0] == hand[4][0]))
    two_pair    = (((hand[0][0] == hand[1][0]) and (hand[2][0] == hand[3][0])) or ((hand[1][0] == hand[2][0]) and (hand[3][0] == hand[4][0])) or ((hand[0][0] == hand[1][0]) and (hand[3][0] == hand[4][0])))

    #Ορισμός του χεριού Royal Flush (δηλαδή πέντε χαρτιά ίδιου τύπου σε σειρά, ξεκινώντας από το 10 και φτάνοντας στον άσσο)
    if (flush) and (straight) and (hand[0][0] == 10):
        return "Royal Flush"

    #Χέρι 'Straight Flush' (χαρτιά σε σειρά με ίδιο τύπο)
    if (flush) and (straight):
        return "Straight Flush"

    #Χέρι Four Of A Kind (self-explanatory)
    if kind_4:
        return "Four Of A Kind"

    #Ορισμός χεριού Full House (ένα ζευγάρι + άλλα τρία ίδια χαρτιά)
    if full_house:
        return "Full House"

    #Ορισμός του χεριού FLUSH (Πέντε ίδιοι τύποι)
    if flush:
        return "Flush"
    
    #Ορισμός του χεριού STRAIGHT (Χαρτιά σε σειρά)
    if straight:
        return "Straight"

    #Ορισμός του χεριού THREE OF A KIND
    if kind_3:
        return "Three Of A Kind"

    if two_pair:
        return "Two Pair"

    #Ορισμός ζευγαριού
    if kind_2:
        return "Pair"
    
def cardBeautifier(hand):
    for card in hand:
        if card[0] == 11:
            card[0] = "J"
        elif card[0] == 12:
            card[0] = "Q"
        elif card[0] == 13:
            card[0] = "K"
        elif card[0] == 14:
            card[0] = "A"
        else:
            card[0] = str(card[0])
    return hand


print("Δείγμα πόκερ. Άσκηση 10, Εισαγωγή στην Επιστήμη των Υπολογιστών, Πανεπιστήμιο Πειραιώς, Π19204\n")
#Ορισμός των καρτών
card_numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]
card_types   = ["Diamonds", "Spades", "Hearts", "Clubs"]
cards        = []

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

player1_cards.sort()
player2_cards.sort()

result1 = whatIsMyHand(player1_cards)
result2 = whatIsMyHand(player2_cards)

player1_cards = cardBeautifier(player1_cards)
player2_cards = cardBeautifier(player2_cards)

random.shuffle(player1_cards)
random.shuffle(player2_cards)

print("Player 1 Cards:", player1_cards, result1)
print("Player 2 Cards:", player2_cards, result2)

print(whoWins(""))