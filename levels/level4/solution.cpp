// Lösung: Beispiel für das Hinzufügen von zwei Zahlen

#include <iostream>

int main() {
    int zahl1, zahl2, summe;
    std::cout << "Gib die erste Zahl ein: ";
    std::cin >> zahl1;
    std::cout << "Gib die zweite Zahl ein: ";
    std::cin >> zahl2;
    summe = zahl1 + zahl2;
    std::cout << "Die Summe ist: " << summe << std::endl;
    return 0;
}
