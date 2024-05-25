# Woche 1-2: Entwicklung und Testen der ersten drei C++-Levels

## Ziel

Die ersten drei C++-Levels sollen die Grundlagen von C++ abdecken, einschließlich Variablen, Datentypen, Ein- und Ausgabe, bedingte Anweisungen und Schleifen.

**Level 4: Grundlagen von C++**

- **Thema**: Variablen und Datentypen
- **Lernziel**: Verständnis der grundlegenden Datentypen und Variablenzuweisung in C++
- **Aufgabe**: Schreibe ein Programm, das zwei Ganzzahlen einliest, sie addiert und das Ergebnis ausgibt.

**Level 5: Einfache mathematische Operationen und Ausgaben**

- **Thema**: Mathematische Operationen und `cout`
- **Lernziel**: Erlernen von mathematischen Operationen und der Nutzung der `cout` Funktion
- **Aufgabe**: Schreibe ein Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.

**Level 6: Bedingte Anweisungen und Schleifen**

- **Thema**: `if`-Anweisungen und `for`-Schleifen
- **Lernziel**: Einführung in Kontrollstrukturen
- **Aufgabe**: Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.

## Woche 1: Entwicklung der Levels

### Level 4: Grundlagen von C++

**Datei: levels/level4/instructions.md**

```markdown
# Level 4: Grundlagen von C++

## Ziel
Verstehe die grundlegenden Datentypen und Variablenzuweisung in C++.

## Aufgabe
Schreibe ein C++-Programm, das zwei Ganzzahlen einliest, sie addiert und das Ergebnis ausgibt.

## Hinweise
- Verwende `std::cin` für die Eingabe.
- Verwende `std::cout` für die Ausgabe.
- Konvertiere die Eingaben bei Bedarf.
```

**Datei: levels/level4/task.cpp**

```cpp
// Aufgabe: Schreibe ein Programm, das zwei Ganzzahlen einliest, sie addiert und das Ergebnis ausgibt.
// Dein Code beginnt hier.

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
```

### Level 5: Einfache mathematische Operationen und Ausgaben

**Datei: levels/level5/instructions.md**

```markdown
# Level 5: Einfache mathematische Operationen und Ausgaben

## Ziel
Lerne, mathematische Operationen durchzuführen und Ergebnisse auszugeben.

## Aufgabe
Schreibe ein C++-Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.

## Hinweise
- Verwende `std::cin` für die Eingabe.
- Verwende `std::cout` für die Ausgabe.
```

**Datei: levels/level5/task.cpp**

```cpp
// Aufgabe: Schreibe ein Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.
// Dein Code beginnt hier.

#include <iostream>

int main() {
    int zahl1, zahl2, produkt;
    std::cout << "Gib die erste Zahl ein: ";
    std::cin >> zahl1;
    std::cout << "Gib die zweite Zahl ein: ";
    std::cin >> zahl2;
    produkt = zahl1 * zahl2;
    std::cout << "Das Produkt ist: " << produkt << std::endl;
    return 0;
}
```

### Level 6: Bedingte Anweisungen und Schleifen

**Datei: levels/level6/instructions.md**

```markdown
# Level 6: Bedingte Anweisungen und Schleifen

## Ziel
Verstehe die Verwendung von `if`-Anweisungen und `for`-Schleifen.

## Aufgabe
Schreibe ein C++-Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.

## Hinweise
- Verwende eine `for`-Schleife, um die Zahlen von 1 bis 10 zu durchlaufen.
- Verwende eine `if`-Anweisung, um zu überprüfen, ob eine Zahl gerade oder ungerade ist.
```

**Datei: levels/level6/task.cpp**

```cpp
// Aufgabe: Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.
// Dein Code beginnt hier.

#include <iostream>

int main() {
    for (int i = 1; i <= 10; ++i) {
        if (i % 2 == 0) {
            std::cout << i << " ist gerade." << std::endl;
        } else {
            std::cout << i << " ist ungerade." << std::endl;
        }
    }
    return 0;
}
```

## Woche 2: Testen der Levels

1. **Testen der Anweisungen und Aufgaben**
   - Stelle sicher, dass die Anweisungen klar und verständlich sind.
   - Teste die Beispielcodes und Aufgaben, um sicherzustellen, dass sie korrekt funktionieren.

2. **Feedback einholen**
   - Lasse Freunde oder Kollegen die Levels ausprobieren und sammle Feedback.
   - Achte auf Verständlichkeit der Aufgaben, Korrektheit der Ergebnisse und allgemeine Benutzerfreundlichkeit.

3. **Verbesserungen und Fehlerbehebung**
   - Implementiere basierend auf dem Feedback notwendige Änderungen und Verbesserungen.
   - Behebe eventuelle Fehler und teste erneut.

### Beispiel für das Testen

**Datei: tests/test_levels.py**

```python
import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    result = subprocess.run(["g++", f"levels/level{level}/task.cpp", "-o", f"levels/level{level}/task.out"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Fehler beim Kompilieren von Level {level}: {result.stderr}")
        return False
    result = subprocess.run([f"./levels/level{level}/task.out"], capture_output=True, text=True)
    print(f"Ausgabe von Level {level}:\n{result.stdout}")
    return True

def main():
    for level in range(4, 7):
        if not run_test(level):
            print(f"Level {level} Test fehlgeschlagen.")
        else:
            print(f"Level {level} Test erfolgreich.")

if __name__ == "__main__":
    main()
```

### Zusammenfassung

In den ersten zwei Wochen konzentrierst du dich auf die Entwicklung und das Testen der ersten drei C++-Levels. Diese Levels decken die Grundlagen von C++ ab und legen den Grundstein für fortgeschrittenere Themen. Achte darauf, Feedback zu sammeln und basierend darauf Anpassungen vorzunehmen, um die Benutzererfahrung zu verbessern.
