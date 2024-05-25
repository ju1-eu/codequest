# Spielkonzept: CodeQuest Terminal Edition

### Spielidee

**CodeQuest Terminal Edition** ist ein Abenteuerspiel, bei dem Spieler durch verschiedene Welten reisen und Programmieraufgaben lösen müssen, um voranzukommen. Das Spiel ist in mehrere Levels unterteilt, wobei jedes Level eine neue Programmiertechnik oder ein neues Konzept vorstellt. Die Spieler lernen durch interaktive Aufgaben und erhalten sofortiges Feedback zu ihrem Code.

### Zielgruppe

- Anfänger bis leicht Fortgeschrittene in der Programmierung
- Altersgruppe: 12+ (kann angepasst werden)

### Spielmechanik

1. **Einführung und Tutorial**
   - Einführung in die Grundlagen von Python und C++
   - Erklärung der Spielmechanik und der Benutzeroberfläche
   - Kurzes Tutorial zur Nutzung des Terminals und von VSCode

2. **Levelstruktur**
   - **Level 1-3**: Grundlagen von Python
     - Syntax, Variablen, einfache Datentypen
     - Aufgaben: Schreibe ein Programm zur Berechnung einfacher mathematischer Probleme
   - **Level 4-6**: Grundlagen von C++
     - Syntax, Variablen, einfache Datentypen, Ein- und Ausgabe
     - Aufgaben: Schreibe ein Programm zur Berechnung einfacher mathematischer Probleme

3. **Algorithmische Problemlösung**
   - **Level 7-9**: Einführung in Algorithmen
     - Sortieralgorithmen (Bubble Sort, Selection Sort)
     - Aufgaben: Implementiere und teste verschiedene Sortieralgorithmen
   - **Level 10-12**: Suchalgorithmen
     - Lineare Suche, Binäre Suche
     - Aufgaben: Schreibe Programme zur Implementierung und Anwendung dieser Algorithmen

4. **Struktogramme und Programmausführung**
   - **Level 13-15**: Struktogramme erstellen und nutzen
     - Einführung in Struktogramme (Nassi-Shneiderman-Diagramme)
     - Aufgaben: Erstelle Struktogramme für gegebene Probleme und schreibe den entsprechenden Code
   - **Level 16-18**: Sinnvolle Programmnamen und Kommentare
     - Best Practices für das Schreiben von sauberem und verständlichem Code
     - Aufgaben: Überarbeite bestehenden Code, füge Kommentare hinzu und benenne Variablen sinnvoll

5. **Projektbasiertes Lernen**
   - **Level 19-21**: Mini-Projekte in Python
     - Erstellen eines kleinen Spiels oder einer Anwendung
   - **Level 22-24**: Mini-Projekte in C++
     - Entwickeln eines kleinen Spiels oder einer Anwendung

### Interaktive Elemente

1. **Hinweise und Tipps**
   - Kontextsensitive Hinweise, die den Spielern helfen, wenn sie feststecken
   - Textbasierte Tutorials und erklärende Dokumente für komplexere Themen

2. **Belohnungssystem**
   - Punkte und Abzeichen für abgeschlossene Aufgaben und Projekte
   - Fortschrittsanzeige, um den Lernfortschritt zu visualisieren

3. **Code-Editor und Terminal**
   - Verwendung von VSCode für das Schreiben und Testen von Code
   - Integration mit dem Terminal für die Ausführung und Fehlersuche

4. **Community-Features**
   - Möglichkeit, Lösungen und Projekte mit anderen Spielern zu teilen
   - Foren und Diskussionsgruppen für Zusammenarbeit und Hilfe

### Lernziele

- Beherrschen der grundlegenden Syntax und Konzepte von Python und C++
- Verständnis für algorithmische Problemlösung
- Fähigkeit, Struktogramme zu erstellen und zu nutzen
- Best Practices für sauberen und gut dokumentierten Code

### Umsetzung

#### Technische Anforderungen

- Entwicklungsumgebung: VSCode und macOS Terminal
- Sprachen: Python, C++
- Tools: Git für Versionskontrolle, Markdown für Dokumentation

#### Team

- **Projektmanager**: Koordination des Teams und der Entwicklungsphasen
- **Entwickler**: Programmierer für die Spielentwicklung, Backend-Entwicklung
- **Pädagogischer Berater**: Sicherstellung der didaktischen Qualität des Spiels

#### Beispiel eines Levels

**Level 1: Einführung in Python**:

- **Ziel**: Lerne die Grundlagen der Python-Syntax, Variablen und einfache Datentypen.
- **Aufgabe**: Schreibe ein Python-Programm, das zwei Zahlen addiert und das Ergebnis ausgibt.
- **Hinweis**: Verwende `input()` für die Eingabe und `print()` für die Ausgabe.

```python
# Beispielcode
zahl1 = input("Gib die erste Zahl ein: ")
zahl2 = input("Gib die zweite Zahl ein: ")
summe = int(zahl1) + int(zahl2)
print("Die Summe ist:", summe)
```

### Zusammenfassung

**CodeQuest Terminal Edition** bietet eine strukturierte und unterhaltsame Möglichkeit, die Grundlagen der Programmierung in Python und C++ zu erlernen. Durch die Nutzung von Terminal und VSCode wird das Lernen praxisnah und realitätsnah gestaltet.

## Nächste Schritte

1. **Projektstruktur und -planung**
   - Definiere die Gesamtstruktur des Spiels: Anzahl der Levels, Lernziele für jedes Level, und die Reihenfolge der Themen.
   - Erstelle eine Roadmap mit Meilensteinen und Zeitplänen für die Entwicklung.

2. **Einrichtung der Entwicklungsumgebung**
   - Stelle sicher, dass du VSCode und das Terminal auf deinem macOS vollständig eingerichtet hast.
   - Installiere notwendige Erweiterungen in VSCode, wie Python und C++ Extensions, und richte ein Git-Repository für die Versionskontrolle ein.

3. **Grundlegende Spiellogik und Benutzeroberfläche**
   - Entwickle eine einfache Benutzerschnittstelle im Terminal, die es ermöglicht, zwischen den Levels zu navigieren und Aufgaben zu sehen.
   - Erstelle eine einfache Menüstruktur für die Auswahl von Levels und das Anzeigen des Fortschritts.

4. **Entwicklung der ersten Levels**
   - Beginne mit den ersten Python-Levels, in denen grundlegende Konzepte wie Variablen und Datentypen eingeführt werden.
   - Implementiere die Mechanik für Aufgaben, bei denen der Spieler Code eingibt und sofortiges Feedback erhält.

5. **Feedback und Anpassungen**
   - Teste die ersten Levels selbst und erhalte Feedback von Freunden oder Kollegen.
   - Passe die Spiellogik und die Benutzeroberfläche basierend auf dem Feedback an.

6. **Erweiterung auf C++ und fortgeschrittene Themen**
   - Entwickle die Levels weiter, indem du C++ einführst und komplexere Programmierkonzepte wie Algorithmen und Struktogramme behandelst.
   - Füge interaktive Tutorials und Hilfsfunktionen hinzu, um die Lernkurve zu unterstützen.

### Beispiel für die Projektstruktur

#### Verzeichnisstruktur

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
│   └── ...
├── scripts/
│   ├── game.py
│   └── utils.py
├── tests/
│   └── test_levels.py
└── .vscode/
    ├── settings.json
    └── launch.json
```

#### Beispiel für ein Level (Level 1)

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

### Starten des Spiels

**Datei: game.py**

```python
import os

def load_level(level_number):
    with open(f"levels/level{level_number}/instructions.md") as f:
        instructions = f.read()
    print(instructions)
    # Weitere Logik zum Laden des Levels und Überprüfen des Codes

def main():
    print("Willkommen bei CodeQuest Terminal Edition!")
    while True:
        level_number = input("Wähle ein Level (oder 'exit' zum Beenden): ")
        if level_number.lower() == 'exit':
            break
        if os.path.exists(f"levels/level{level_number}"):
            load_level(level_number)
        else:
            print("Level nicht gefunden. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
```

### Feedback und Iteration

- **Testen**: Stelle sicher, dass du die Levels testest und das Feedback berücksichtigst, um das Spiel zu verbessern.
- **Dokumentation**: Halte eine gute Dokumentation und Anleitungen bereit, um den Einstieg für die Spieler zu erleichtern.
- **Community**: Ermutige die Spieler, ihre Lösungen und Erfahrungen zu teilen, um eine aktive Lerncommunity zu schaffen.


