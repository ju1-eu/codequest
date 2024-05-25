# Aufgabe: Erweitere den Code aus Level 16, um Fehlerbehandlung und Debugging-Informationen hinzuzufügen.
# Dein Code beginnt hier

def summe_berechnen(zahl1, zahl2):
    return zahl1 + zahl2

def produkt_berechnen(zahl1, zahl2):
    return zahl1 * zahl2

def main():
    try:
        # Eingabe der ersten Zahl
        zahl1 = int(input("Geben Sie die erste Zahl ein: "))
        # Eingabe der zweiten Zahl
        zahl2 = int(input("Geben Sie die zweite Zahl ein: "))

        # Debugging-Ausgabe
        print(f"Debug: Eingaben sind {zahl1} und {zahl2}")

        # Berechnung und Ausgabe der Summe
        summe = summe_berechnen(zahl1, zahl2)
        print(f"Die Summe ist: {summe}")

        # Berechnung und Ausgabe des Produkts
        produkt = produkt_berechnen(zahl1, zahl2)
        print(f"Das Produkt ist: {produkt}")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie ganze Zahlen ein.")

if __name__ == "__main__":
    main()
