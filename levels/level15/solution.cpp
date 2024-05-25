// Lösung: Verbessere den Code aus Level 14 durch Hinzufügen sinnvoller Programmnamen und Kommentare.

#include <iostream>

// Hauptfunktion
int main() {
    int ersteZahl, zweiteZahl, summe;

    // Eingabe der ersten Zahl
    std::cout << "Geben Sie die erste Zahl ein: ";
    std::cin >> ersteZahl;

    // Eingabe der zweiten Zahl
    std::cout << "Geben Sie die zweite Zahl ein: ";
    std::cin >> zweiteZahl;

    // Berechnung der Summe
    summe = ersteZahl + zweiteZahl;

    // Ausgabe der Summe
    std::cout << "Die Summe ist: " << summe << std::endl;

    return 0;
}
