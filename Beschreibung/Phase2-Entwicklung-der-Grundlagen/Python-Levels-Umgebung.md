# Python

## Schritt 1: Python installieren

Stelle sicher, dass Python 3.x auf deinem System installiert ist. Du kannst die neueste Version von [python.org](https://www.python.org/downloads/) herunterladen und installieren.

## Schritt 2: Virtuelle Umgebung einrichten

Es wird empfohlen, eine virtuelle Umgebung für dein Projekt zu erstellen, um Abhängigkeiten isoliert zu halten.

1. Navigiere zu deinem Projektverzeichnis.

```sh
cd path/to/codequest
```

2. Erstelle eine virtuelle Umgebung.

```sh
python -m venv venv
```

3. Aktiviere die virtuelle Umgebung.

   - Auf Windows:

   ```sh
   venv\Scripts\activate
   ```

   - Auf macOS und Linux:

   ```sh
   source venv/bin/activate
   ```

## Schritt 3: Abhängigkeiten installieren

Erstelle eine `requirements.txt`-Datei, um die benötigten Python-Pakete aufzulisten. Für dieses Projekt könnte es sinnvoll sein, grundlegende Pakete wie `pytest` für Tests oder `numpy` für erweiterte numerische Operationen hinzuzufügen, wenn benötigt.

**Datei: requirements.txt**

```plaintext
pytest
```

Installiere die Abhängigkeiten mit pip:

```sh
pip install -r requirements.txt
```

## Schritt 4: Projektverzeichnisstruktur

Stelle sicher, dass dein Projektverzeichnis die richtige Struktur hat:

```plaintext
codequest/
├── README.md
├── LICENSE
├── requirements.txt
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

## Schritt 5: Hauptspielskript (`game.py`)

Erstelle das Hauptspielskript, das die Level lädt und das Spiel steuert.

**Datei: scripts/game.py**

```python
import os

def load_level(level_number):
    language = 'python' if level_number <= 3 else 'cpp'

    if language == 'python':
        file_extension = 'py'
        instructions_path = f"levels/level{level_number}/instructions.md"
        task_path = f"levels/level{level_number}/task.{file_extension}"
        try:
            with open(instructions_path) as f:
                instructions = f.read()
            print(instructions)
            os.system(f"python {task_path}")
        except FileNotFoundError:
            print(f"Level {level_number} nicht gefunden.")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
    else:
        instructions_path = f"levels/level{level_number}/instructions.md"
        makefile_path = f"levels/level{level_number}/Makefile"
        try:
            with open(instructions_path) as f:
                instructions = f.read()
            print(instructions)
            os.system(f"make -C levels/level{level_number}")
            os.system(f"make -C levels/level{level_number} run")
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

## Schritt 6: Tests für Levels

Erstelle ein Testskript, um die Levels zu testen.

**Datei: tests/test_levels.py**

```python
import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    file_extension = 'py' if level <= 3 else 'cpp'
    if file_extension == 'py':
        command = ["python", f"levels/level{level}/task.py"]
    else:
        command = ["make", "-C", f"levels/level{level}", "run"]

    result = subprocess.run(command, capture_output=True, text=True)
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

## Schritt 7: Ausführen und Testen

1. Stelle sicher, dass die virtuelle Umgebung aktiviert ist:

   - Auf Windows:

   ```sh
   venv\Scripts\activate
   ```

   - Auf macOS und Linux:

   ```sh
   source venv/bin/activate
   ```

2. Starte das Hauptspiel:

```sh
python scripts/game.py
```

3. Teste die Levels:

```sh
python tests/test_levels.py
```

## Zusammenfassung

Diese Schritte helfen dir, Python für dein Lernspiel einzurichten und zu nutzen. Mit der Erstellung und Nutzung einer virtuellen Umgebung, der Installation von Abhängigkeiten und der Einrichtung von Skripten für das Spiel und die Tests kannst du eine saubere und gut organisierte Entwicklungsumgebung sicherstellen.
