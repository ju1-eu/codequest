# Aufgabe: Erstelle ein Struktogramm für ein Programm, das die Summe von zwei Zahlen berechnet und das Ergebnis ausgibt.
# Dein Code beginnt hier

def main():
    try:
        zahl1 = int(input("Geben Sie die erste Zahl ein: "))
        zahl2 = int(input("Geben Sie die zweite Zahl ein: "))

        summe = zahl1 + zahl2

        print(f"Die Summe ist: {summe}")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie ganze Zahlen ein.")

if __name__ == "__main__":
    main()
