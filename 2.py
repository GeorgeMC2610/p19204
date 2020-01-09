print("Η είσοδος του κειμένου γίνεται μέσω του αρχείου 2.txt")
txtfile         = open("2.txt", "r")
words           = txtfile.read()
words           = words.split(" ")
badLetters      = ["f", "c", "k", "r"]
otherConsonants = ["b", "d", "g", "h", "j", "l", "m", "n", "p", "q", "s", "t", "v", "w", "x", "z"]

for word in words:
    badCounter = 0
    normalCounter = 0
    for letter in word:
        if letter in badLetters:
            badCounter += 1
        if letter in otherConsonants:
            normalCounter += 1
    
    if badCounter >= normalCounter:
        print("Found bad word: " + word)
