print("Η εισαγωγή των λέξεων γίνεται μέσω του αρχείου 1.txt.")

txtfile = open("1.txt", "r")
words   = txtfile.read()
words   = words.split()

biggestWords = []
vowels = ["e", "y", "u", "i", "o", "a"]

#Εύρεση των πέντε μεγαλύτερων λέξεων.
for i in range(0,5):
    biggestWord = ""
    counter = 0

    for testWord in words:

        if len(testWord) > len(biggestWord):
            biggestWord = testWord 
            position = counter
        counter += 1   
    else:
        biggestWords.append(biggestWord)
        words.pop(position)
print("Οι μεγαλύτερες λέξεις είναι:", biggestWords)

for testWord in biggestWords:
    for letter in testWord:
        if letter in vowels: