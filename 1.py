print("Η εισαγωγή των λέξεων γίνεται μέσω του αρχείου 1.txt.")

def findBiggestWord(words):
    biggestWord = words[0]
    for testWord in words:
        if len(word) > len(biggestWord):
            biggestWord = testWord

    
    return biggestWord

    


txtfile = open("1.txt", "r")
words   = txtfile.read()
words   = words.split(" ")

biggestWords = ["", "", "", "", ""]
for i in range(0,5):
    biggestWords.append(findBiggestWord(words))

print


    