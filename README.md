# CodeQuest Terminal Edition

**CodeQuest Terminal Edition** ist ein Lernspiel, das darauf abzielt, Anfängern die Grundlagen der Programmierung in Python und C++ beizubringen. Das Spiel führt die Spieler durch verschiedene Levels, in denen sie Programmieraufgaben lösen müssen, um voranzukommen. Jedes Level stellt neue Programmierkonzepte vor und bietet praktische Übungen, um das Verständnis zu vertiefen.

## Inhalte

- **Level 1-3**: Grundlagen von Python
  - Variablen und Datentypen
  - Mathematische Operationen und Ausgaben
  - Bedingte Anweisungen und Schleifen

- **Level 4-6**: Grundlagen von C++
  - Variablen und Datentypen
  - Mathematische Operationen und Ausgaben
  - Bedingte Anweisungen und Schleifen

## Verzeichnisstruktur

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

## Installation und Ausführung

### Voraussetzungen

- Python 3.x
- g++ (für C++-Level)
- Make (für C++-Level)

### Installation

1. Klone das Repository:
    ```sh
    git clone https://github.com/username/codequest.git
    cd codequest
    ```

2. Installiere notwendige Python-Pakete (falls benötigt):
    ```sh
    pip install -r requirements.txt
    ```

### Ausführung

1. Starte das Spiel:
    ```sh
    python scripts/game.py
    ```

2. Folge den Anweisungen im Terminal, um die verschiedenen Levels zu spielen.

## Mitwirken

Beiträge sind willkommen! Bitte erstelle einen neuen Branch für deine Änderungen und sende einen Pull-Request.

1. Forke das Repository.
2. Erstelle einen neuen Branch:
    ```sh
    git checkout -b feature/DeinFeature
    ```
3. Führe deine Änderungen durch und committe:
    ```sh
    git commit -m "Beschreibung deiner Änderungen"
    ```
4. Schiebe deinen Branch:
    ```sh
    git push origin feature/DeinFeature
    ```
5. Erstelle einen Pull-Request auf GitHub.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE)-Datei für weitere Informationen.
