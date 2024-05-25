// Aufgabe: Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.
// Dein Code beginnt hier.

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
