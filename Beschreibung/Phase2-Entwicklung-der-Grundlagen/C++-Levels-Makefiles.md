# Makefiles

## Schritt 1: Erstellen eines Makefiles

Erstelle für jedes C++-Level ein Makefile, das die Kompilierung und Ausführung des Programms ermöglicht.

### Beispiel für Level 4

**Datei: levels/level4/Makefile**

```makefile
# Makefile für Level 4

# Compiler und Compiler-Flags
CXX = g++
CXXFLAGS = -Wall -std=c++11

# Zieldatei
TARGET = task

# Standardziel
all: $(TARGET)

# Regel zur Kompilierung
$(TARGET): task.cpp
	$(CXX) $(CXXFLAGS) task.cpp -o $(TARGET)

# Regel zur Ausführung
run: $(TARGET)
	./$(TARGET)

# Regel zum Löschen der erzeugten Dateien
clean:
	rm -f $(TARGET)
```

### Wiederhole diesen Schritt für Level 5 und Level 6

Erstelle ähnliche Makefiles für die anderen C++-Levels.

**Datei: levels/level5/Makefile**

```makefile
# Makefile für Level 5

CXX = g++
CXXFLAGS = -Wall -std=c++11

TARGET = task

all: $(TARGET)

$(TARGET): task.cpp
	$(CXX) $(CXXFLAGS) task.cpp -o $(TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)
```

**Datei: levels/level6/Makefile**

```makefile
# Makefile für Level 6

CXX = g++
CXXFLAGS = -Wall -std=c++11

TARGET = task

all: $(TARGET)

$(TARGET): task.cpp
	$(CXX) $(CXXFLAGS) task.cpp -o $(TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)
```

## Schritt 2: Kompilieren und Ausführen im Terminal

Navigiere im Terminal zu dem jeweiligen Level-Verzeichnis und verwende Make, um das Programm zu kompilieren und auszuführen.

### Beispiel für Level 4

1. Öffne das Terminal.
2. Navigiere zum Verzeichnis `levels/level4`:

```sh
cd path/to/codequest/levels/level4
```

3. Kompiliere das Programm:

```sh
make
```

4. Führe das Programm aus:

```sh
make run
```

5. Bereinige die erzeugten Dateien (optional):

```sh
make clean
```

### Wiederhole diesen Schritt für Level 5 und Level 6

Navigiere zu den jeweiligen Verzeichnissen und führe die gleichen Make-Befehle aus:

```sh
cd path/to/codequest/levels/level5
make
make run
make clean

cd path/to/codequest/levels/level6
make
make run
make clean
```

### Integration in das Hauptspielskript

Um die Makefiles in das Hauptspielskript zu integrieren, kannst du die `os.system`-Aufrufe anpassen, um Make-Befehle auszuführen.

**Datei: game.py**

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

### Zusammenfassung

Mit Makefiles kannst du die Kompilierung und Ausführung deiner C++-Programme im Terminal automatisieren. Erstelle für jedes C++-Level ein Makefile, das die Kompilierung (`make`) und Ausführung (`make run`) des Programms ermöglicht. Integriere diese Makefiles in dein Hauptspielskript, um den Prozess zu vereinfachen. Dies ermöglicht eine nahtlose Nutzung und Testing der Programme direkt aus dem Terminal.
