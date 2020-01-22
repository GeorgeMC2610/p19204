#Εργασία 9 στο Μάθημα 'Εισαγωγή στην Επιστήμη των Υπολογιστών' p19204
def isNumber(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            x = input("Παρακαλώ δώστε έναν έγκυρο αριθμό: ")

while True:
    x = input("Δώστε έναν θετικό αριθμό: ")
    x = isNumber(x)
    if x > 0:
        break

while True:
    print("Αριθμός εισόδου:", x)
    x *= 3
    x += 1
    print("Τριπλασιασμένος +1 αριθμός:", x)
    a = 0
    for i in str(x):
        a += int(i)
    x = a
    print("Αριθμός με προσθετημένα ψηφία:", x, "\n")
    if len(str(x)) == 1:
        break

print("Η Διαδικασία τελείωσε!")