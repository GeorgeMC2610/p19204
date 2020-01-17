import random

def whatIsMyHand(hand):
    #Κάποια από τα χέρια βγαίνουν από τον συνδυασμό μερικών άλλων, π.χ. το Royal Flush
    #Πλήρης έλεγχος στα χαρτιά, καθώς είναι σε αύξουσα σειρά
    #Το χέρι FIVE OF A KIND έχει αντικατασταθεί με ROYAL FLUSH, καθώς δεν έχω βάλει τζόκερ στην τράπουλα
    #Όπως, επίσης, δεν έχει υλοποιηθεί το High Card

    straight    = (hand[0][0] == (hand[1][0] - 1)) and (hand[1][0] == (hand[2][0] - 1)) and (hand[2][0] == (hand[3][0] - 1)) and (hand[3][0] == (hand[4][0] - 1))
    flush       = (hand[0][1] == hand[1][1]) and (hand[1][1] == hand[2][1]) and (hand[2][1] == hand[3][1]) and (hand[3][1] == hand[4][1]) and (hand[4][1] == hand[0][1])
    full_house  = ((hand[0][0] == hand[1][0]) and (hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0])) or ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0]) and (hand[3][0] == hand[4][0]))
    kind_4      = ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0])) or ((hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0]))
    kind_3      = ((hand[0][0] == hand[1][0]) and (hand[1][0] == hand[2][0])) or ((hand[1][0] == hand[2][0]) and (hand[2][0] == hand[3][0])) or ((hand[2][0] == hand[3][0]) and (hand[3][0] == hand[4][0]))
    kind_2      = ((hand[0][0] == hand[1][0]) or (hand[1][0] == hand[2][0]) or (hand[2][0] == hand[3][0]) or (hand[3][0] == hand[4][0]))
    two_pair    = (((hand[0][0] == hand[1][0]) and (hand[2][0] == hand[3][0])) or ((hand[1][0] == hand[2][0]) and (hand[3][0] == hand[4][0])) or ((hand[0][0] == hand[1][0]) and (hand[3][0] == hand[4][0])))

    #Ορισμός του χεριού Royal Flush (δηλαδή πέντε χαρτιά ίδιου τύπου σε σειρά, ξεκινώντας από το 10 και φτάνοντας στον άσσο)
    if (flush) and (straight) and (hand[0][0] == 10):
        return ["Royal Flush", 9]

    #Χέρι 'Straight Flush' (χαρτιά σε σειρά με ίδιο τύπο)
    if (flush) and (straight):
        return ["Straight Flush", 8]

    #Χέρι Four Of A Kind (self-explanatory)
    if kind_4:
        return ["Four Of A Kind", 7]

    #Ορισμός χεριού Full House (ένα ζευγάρι + άλλα τρία ίδια χαρτιά)
    if full_house:
        return ["Full House", 6]

    #Ορισμός του χεριού FLUSH (Πέντε ίδιοι τύποι)
    if flush:
        return ["Flush", 5]
    
    #Ορισμός του χεριού STRAIGHT (Χαρτιά σε σειρά)
    if straight:
        return ["Straight", 4]

    #Ορισμός του χεριού THREE OF A KIND
    if kind_3:
        return ["Three Of A Kind", 3]

    if two_pair:
        return ["Two Pair", 2]

    #Ορισμός ζευγαριού
    if kind_2:
        return ["Pair", 1]

    return [None, 0]
    
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

counter = 0
score_1 = 0
score_2 = 0
answer = "y"
while answer == "y":
    counter += 1
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

    #Για debugging, ο παρακάτω κώδικας, με αυτάκια, ορίζει τις κάρτες του παίκτη στην αρέσκειά σας. ΥΠ' ΟΨΙΝ: Τα φύλλα πρέπει να είναι από 2 έως και 14! 14 = ΑΣΣΟΣ, 13 = ΡΗΓΑΣ, 12 = ΝΤΑΜΑ, 11 = ΒΑΛΕΣ
    '''player1_cards = [[10, "Clubs"], [11, "Clubs"], [12, "Clubs"], [13, "Clubs"], [14, "Clubs"]]'''
    '''player2_cards = [[10, "Diamonds"], [11, "Diamonds"], [12, "Diamonds"], [13, "Diamonds"], [14, "Spades"]]'''

    #Κατάταξη των καρτών για εύκολη εύρεση του χεριού
    player1_cards.sort()
    player2_cards.sort()

    #Επιστροφή του αποτελέσματος
    result1 = whatIsMyHand(player1_cards)
    result2 = whatIsMyHand(player2_cards)

    #Παρουσίαση των χαρτιών ανακάτεμα των χεριών για πιο αληθοφανή εφαρμογή
    player1_cards = cardBeautifier(player1_cards)
    player2_cards = cardBeautifier(player2_cards)

    random.shuffle(player1_cards)
    random.shuffle(player2_cards)

    if result1[1] > result2[1]:
        score_1 += 1
    elif result1[1] < result2[1]:
        score_2 += 1

    print("Player 1 Cards:", player1_cards, result1[0])
    print("Player 2 Cards:", player2_cards, result2[0])
    print("\nScore:", score_1, "-", score_2)

    
    answer = input("Play again? y/n: ")

if counter == 1:
    print("Τέλος δείγματος Πόκερ. Έπαιξες, συνολικά, μία φορά.")
else:
    print("Τέλος δείγματος Πόκερ. Έπαιξες, συνολικά,", counter, "φορές.")