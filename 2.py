#Εργασία 2 στο Μάθημα 'Εισαγωγή στην Επιστήμη των Υπολογιστών' p19204

print("Η είσοδος του κειμένου γίνεται μέσω του αρχείου 2.txt")
txtfile         = open("2.txt", "r")
words           = txtfile.read()
words           = words.split()
badLetters      = ["f", "c", "k", "r"]
notConsonants   = ["a", "e", "i", "o", "u", "y", ",", "."]

for word in words:
    badCounter = 0
    normalCounter = 0
    for letter in word:
        if letter in badLetters:
            badCounter += 1
        elif letter not in notConsonants:
            normalCounter += 1
    
    if (badCounter > normalCounter) and (len(word) > 3):
        print("Found potential bad word: " + word)
