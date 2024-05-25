// Lösung: Programm zur Ausgabe von Zahlen und Bestimmung, ob sie gerade oder ungerade sind

#include <iostream>

int main() {
    for (int zahl = 1; zahl <= 10; ++zahl) {
        if (zahl % 2 == 0) {
            std::cout << zahl << " ist gerade." << std::endl;
        } else {
            std::cout << zahl << " ist ungerade." << std::endl;
        }
    }
    return 0;
}