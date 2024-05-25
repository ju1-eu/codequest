# Aufgabe: Erstelle ein Struktogramm für ein Programm, das mehrere Funktionen enthält (z.B. eine Funktion zur Berechnung der Summe und eine zur Berechnung des Produkts von zwei Zahlen).
# Dein Code beginnt hier

def summe_berechnen(zahl1, zahl2):
    return zahl1 + zahl2

def produkt_berechnen(zahl1, zahl2):
    return zahl1 * zahl2

def main():
    # Eingabe der ersten Zahl
    zahl1 = int(input("Geben Sie die erste Zahl ein: "))
    # Eingabe der zweiten Zahl
    zahl2 = int(input("Geben Sie die zweite Zahl ein: "))

    # Berechnung und Ausgabe der Summe
    summe = summe_berechnen(zahl1, zahl2)
    print(f"Die Summe ist: {summe}")

    # Berechnung und Ausgabe des Produkts
    produkt = produkt_berechnen(zahl1, zahl2)
    print(f"Das Produkt ist: {produkt}")

if __name__ == "__main__":
    main()
