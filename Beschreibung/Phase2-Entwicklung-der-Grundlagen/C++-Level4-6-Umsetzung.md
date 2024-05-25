# Grundlagen von C++ (Level 4-6)

## Projektstruktur

```plaintext
codequest/
├── README.md
├── LICENSE
├── levels/
│   ├── level1/
│   │   ├── instructions.md
│   │   ├── task.py
│   │   └── solution.py
│   ├── level2/
│   │   ├── instructions.md
│   │   ├── task.py
│   │   └── solution.py
│   ├── level3/
│   │   ├── instructions.md
│   │   ├── task.py
│   │   └── solution.py
│   ├── level4/
│   │   ├── instructions.md
│   │   ├── task.cpp
│   │   └── solution.cpp
│   ├── level5/
│   │   ├── instructions.md
│   │   ├── task.cpp
│   │   └── solution.cpp
│   ├── level6/
│   │   ├── instructions.md
│   │   ├── task.cpp
│   │   └── solution.cpp
├── scripts/
│   ├── game.py
│   └── utils.py
├── tests/
│   └── test_levels.py
└── .vscode/
    ├── settings.json
    └── launch.json
```

### Level 4: Grundlagen von C++

**Datei: instructions.md**

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

**Datei: task.cpp**

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

**Datei: solution.cpp**

```cpp
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
```

### Level 5: Einfache mathematische Operationen und Ausgaben

**Datei: instructions.md**

```markdown
# Level 5: Einfache mathematische Operationen und Ausgaben

## Ziel
Erlernen von mathematischen Operationen und der Nutzung der `std::cout` Funktion.

## Aufgabe
Schreibe ein C++-Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.

## Hinweise
- Verwende `std::cin` für die Eingabe.
- Verwende `std::cout` für die Ausgabe.
- Konvertiere die Eingaben bei Bedarf.
```

**Datei: task.cpp**

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

**Datei: solution.cpp**

```cpp
// Lösung: Beispiel für die Multiplikation von zwei Zahlen

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

**Datei: instructions.md**

```markdown
# Level 6: Bedingte Anweisungen und Schleifen

## Ziel
Einführung in Kontrollstrukturen wie `if`-Anweisungen und `for`-Schleifen.

## Aufgabe
Schreibe ein C++-Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.

## Hinweise
- Verwende eine `for`-Schleife, um die Zahlen von 1 bis 10 zu durchlaufen.
- Verwende eine `if`-Anweisung, um zu überprüfen, ob eine Zahl gerade oder ungerade ist.
```

**Datei: task.cpp**

```cpp
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
```

**Datei: solution.cpp**

```cpp
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
```

### Integration in das Hauptspiel

**Datei: game.py**

Füge den neuen C++-Level-Ladeprozess hinzu:

```python
import os

def load_level(level_number):
    language = 'python' if level_number <= 3 else 'cpp'
    file_extension = 'py' if language == 'python' else 'cpp'

    instructions_path = f"levels/level{level_number}/instructions.md"
    task_path = f"levels/level{level_number}/task.{file_extension}"

    try:
        with open(instructions_path) as f:
            instructions = f.read()
        print(instructions)

        if language == 'python':
            os.system(f"python {task_path}")
        else:
            os.system(f"g++ {task_path} -o levels/level{level_number}/task.out && levels/level{level_number}/task.out")
    except FileNotFoundError:
        print(f"Level {level_number} nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def main():
    print("Willkommen bei CodeQuest Terminal Edition!")
    while True:
        level_number = input("Wähle ein Level (oder 'exit' zum Beenden): ")
        if level_number.lower() == 'exit':
            break
        if level_number.isdigit() and int(level_number) in range(1, 7):
            load_level(level_number)
        else:
            print("Level nicht gefunden. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
```

### Testen der Levels

**Datei: test_levels.py**

Erweitere das Testskript, um C++-Levels zu unterstützen:

```python
import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    file_extension = 'py' if level <= 3 else 'cpp'
    command = ["python", f"levels/level{level}/task.py"] if level <= 3 else ["g++", f"levels/level{level}/task.cpp", "-o", f"levels/level{level}/task.out"]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Fehler beim Kompilieren/Ausführen von

 Level {level}: {result.stderr}")
        return False
    if level > 3:
        result = subprocess.run([f"levels/level{level}/task.out"], capture_output=True, text=True)

    print(f"Ausgabe von Level {level}:\n{result.stdout}")
    return result.returncode == 0

def main():
    for level in range(1, 7):
        if not run_test(level):
            print(f"Level {level} Test fehlgeschlagen.")
        else:
            print(f"Level {level} Test erfolgreich.")

if __name__ == "__main__":
    main()
```

### Zusammenfassung

Mit dieser erweiterten Struktur und den Dateien kannst du die Grundlagen von C++ (Level 4-6) umsetzen. Jedes Level enthält eine Anleitung (instructions.md), eine Aufgabe (task.cpp) und eine Lösung (solution.cpp). Das Hauptspielskript (game.py) lädt die Level und zeigt die Anweisungen an. Ein erweitertes Testskript (test_levels.py) ermöglicht das Testen der Aufgaben in Python und C++. Diese Struktur hilft Anfängern, die Grundlagen von C++ zu erlernen und ihre Programmierfähigkeiten schrittweise zu entwickeln.
