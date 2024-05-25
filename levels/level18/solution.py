# Lösung: Führe ein Code-Review für den Code aus Level 17 durch und verbessere ihn durch Refactoring.

def berechne_summe(zahl1, zahl2):
    return zahl1 + zahl2

def berechne_produkt(zahl1, zahl2):
    return zahl1 * zahl2

def eingabe_zahl(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("Ungültige Eingabe.")

def main():
    try:
        zahl1 = eingabe_zahl("Geben Sie die erste Zahl ein: ")
        zahl2 = eingabe_zahl("Geben Sie die zweite Zahl ein: ")

        print(f"Debug: Eingaben sind {zahl1} und {zahl2}")

        summe = berechne_summe(zahl1, zahl2)
        print(f"Die Summe ist: {summe}")

        produkt = berechne_produkt(zahl1, zahl2)
        print(f"Das Produkt ist: {produkt}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
