# Grundlagen von Python (Level 1-3) im Projekt umsetzen

## Projektstruktur

Zuerst definieren wir die Verzeichnisstruktur deines Projekts:

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
├── scripts/
│   ├── game.py
│   └── utils.py
├── tests/
│   └── test_levels.py
└── .vscode/
    ├── settings.json
    └── launch.json
```

### Level 1: Einführung in Python

**Datei: instructions.md**

```markdown
# Level 1: Einführung in Python

## Ziel
Lerne die Grundlagen der Python-Syntax, Variablen und einfache Datentypen.

## Aufgabe
Schreibe ein Python-Programm, das zwei Zahlen addiert und das Ergebnis ausgibt.

## Hinweise
- Verwende `input()` für die Eingabe.
- Verwende `print()` für die Ausgabe.
- Konvertiere die Eingaben in Ganzzahlen mit `int()`.
```

**Datei: task.py**

```python
# Aufgabe: Schreibe ein Programm, das zwei Zahlen addiert und das Ergebnis ausgibt.
# Dein Code beginnt hier.

# Eingabe der ersten Zahl
zahl1 = input("Gib die erste Zahl ein: ")
# Eingabe der zweiten Zahl
zahl2 = input("Gib die zweite Zahl ein: ")

# Berechnung der Summe
summe = int(zahl1) + int(zahl2)

# Ausgabe des Ergebnisses
print("Die Summe ist:", summe)
```

**Datei: solution.py**

```python
# Lösung: Beispiel für das Hinzufügen von zwei Zahlen

zahl1 = input("Gib die erste Zahl ein: ")
zahl2 = input("Gib die zweite Zahl ein: ")
summe = int(zahl1) + int(zahl2)
print("Die Summe ist:", summe)
```

### Level 2: Einfache mathematische Operationen und Ausgaben

**Datei: instructions.md**

```markdown
# Level 2: Einfache mathematische Operationen und Ausgaben

## Ziel
Erlernen von mathematischen Operationen und der Nutzung der `print()` Funktion.

## Aufgabe
Schreibe ein Python-Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.

## Hinweise
- Verwende `input()` für die Eingabe.
- Verwende `print()` für die Ausgabe.
- Konvertiere die Eingaben in Ganzzahlen mit `int()`.
```

**Datei: task.py**

```python
# Aufgabe: Schreibe ein Programm, das zwei Zahlen multipliziert und das Ergebnis ausgibt.
# Dein Code beginnt hier.

# Eingabe der ersten Zahl
zahl1 = input("Gib die erste Zahl ein: ")
# Eingabe der zweiten Zahl
zahl2 = input("Gib die zweite Zahl ein: ")

# Berechnung des Produkts
produkt = int(zahl1) * int(zahl2)

# Ausgabe des Ergebnisses
print("Das Produkt ist:", produkt)
```

**Datei: solution.py**

```python
# Lösung: Beispiel für die Multiplikation von zwei Zahlen

zahl1 = input("Gib die erste Zahl ein: ")
zahl2 = input("Gib die zweite Zahl ein: ")
produkt = int(zahl1) * int(zahl2)
print("Das Produkt ist:", produkt)
```

### Level 3: Bedingte Anweisungen und Schleifen

**Datei: instructions.md**

```markdown
# Level 3: Bedingte Anweisungen und Schleifen

## Ziel
Einführung in Kontrollstrukturen wie `if`-Anweisungen und `for`-Schleifen.

## Aufgabe
Schreibe ein Python-Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.

## Hinweise
- Verwende eine `for`-Schleife, um die Zahlen von 1 bis 10 zu durchlaufen.
- Verwende eine `if`-Anweisung, um zu überprüfen, ob eine Zahl gerade oder ungerade ist.
```

**Datei: task.py**

```python
# Aufgabe: Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.
# Dein Code beginnt hier.

# Schleife über die Zahlen von 1 bis 10
for zahl in range(1, 11):
    # Bedingte Anweisung zur Überprüfung, ob die Zahl gerade ist
    if zahl % 2 == 0:
        print(zahl, "ist gerade.")
    else:
        print(zahl, "ist ungerade.")
```

**Datei: solution.py**

```python
# Lösung: Programm zur Ausgabe von Zahlen und Bestimmung, ob sie gerade oder ungerade sind

for zahl in range(1, 11):
    if zahl % 2 == 0:
        print(zahl, "ist gerade.")
    else:
        print(zahl, "ist ungerade.")
```

### Starten des Spiels

**Datei: game.py**

```python
import os

def load_level(level_number):
    try:
        with open(f"levels/level{level_number}/instructions.md") as f:
            instructions = f.read()
        print(instructions)
        # Weitere Logik zum Laden des Levels und Überprüfen des Codes
    except FileNotFoundError:
        print(f"Level {level_number} nicht gefunden.")

def main():
    print("Willkommen bei CodeQuest Terminal Edition!")
    while True:
        level_number = input("Wähle ein Level (oder 'exit' zum Beenden): ")
        if level_number.lower() == 'exit':
            break
        if level_number.isdigit() and int(level_number) in range(1, 4):
            load_level(level_number)
        else:
            print("Level nicht gefunden. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
```

### Testen der Levels

**Datei: test_levels.py**

```python
import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    result = subprocess.run(["python", f"levels/level{level}/task.py"], capture_output=True, text=True)
    print(f"Ausgabe von Level {level}:\n{result.stdout}")
    return result.returncode == 0

def main():
    for level in range(1, 4):
        if not run_test(level):
            print(f"Level {level} Test fehlgeschlagen.")
        else:
            print(f"Level {level} Test erfolgreich.")

if __name__ == "__main__":
    main()
```

### Zusammenfassung

Mit dieser Struktur und diesen Dateien kannst du die ersten drei Levels deines Lernspiels umsetzen. Jedes Level enthält eine Anleitung (instructions.md), eine Aufgabe (task.py) und eine Lösung (solution.py). Das Hauptspielskript (game.py) lädt die Level und zeigt die Anweisungen an. Ein Testskript (test_levels.py) ermöglicht das Testen der Aufgaben. Diese Struktur hilft Anfängern, die Grundlagen von Python zu erlernen und ihre Programmierfähigkeiten schrittweise zu entwickeln.