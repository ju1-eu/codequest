# Schritt 1: Struktur des Fortschrittsdatensatzes

Zuerst definieren wir die Struktur des JSON-Datensatzes, der den Fortschritt eines Spielers speichert. `progress.json`

```json
{
  "player_name": "Jan",
  "completed_levels": {
    "Python": [1, 2, 3],
    "C++": [4, 5, 6],
    "Algorithms": [7, 8, 9, 10, 11, 12],
    "Struktogramme": [13, 14, 15, 16, 17, 18],
    "Projects": [19, 20, 21, 22, 23, 24]
  }
}
```

## Schritt 2: Speichern des Fortschritts in einer JSON-Datei

Erstelle eine Python-Datei `progress.py`, die Funktionen zum Laden und Speichern des Fortschritts enthält:

```python
import json
import os

PROGRESS_FILE = "progress.json"

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {
            "player_name": "",
            "completed_levels": {
                "Python": [],
                "C++": [],
                "Algorithms": [],
                "Struktogramme": [],
                "Projects": []
            }
        }
    with open(PROGRESS_FILE, "r") as file:
        return json.load(file)

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as file:
        json.dump(progress, file, indent=4)

def mark_level_completed(language, level):
    progress = load_progress()
    if level not in progress["completed_levels"][language]:
        progress["completed_levels"][language].append(level)
    save_progress(progress)

def display_progress():
    progress = load_progress()
    print(f"Spieler: {progress['player_name']}")
    for category, levels in progress["completed_levels"].items():
        print(f"{category}: Abgeschlossene Levels: {levels}")

def set_player_name(name):
    progress = load_progress()
    progress["player_name"] = name
    save_progress(progress)
```

## Schritt 3: Integration der Fortschrittsanzeige ins Spiel

Integriere die Fortschrittsanzeige und das Markieren abgeschlossener Levels in dein Hauptspielskript `game.py`:

```python
import os
import subprocess
from progress import load_progress, save_progress, mark_level_completed, display_progress, set_player_name

def load_level(level_number):
    level_number = int(level_number)  # Konvertiere level_number in eine Ganzzahl
    language = determine_language_for_level(level_number)
    instructions_path = f"levels/level{level_number}/instructions.md"

    try:
        with open(instructions_path) as f:
            instructions = f.read()
        print(instructions)

        if language == "Python":
            task_path = f"levels/level{level_number}/task.py"
            os.system(f"python {task_path}")
        else:
            print(f"Führe 'make clean' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "clean"], check=True)

            print(f"Führe 'make' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}"], check=True)

            print(f"Führe 'make run' für Level {level_number} aus...")

            # Öffne ein Pseudo-Terminal für Benutzereingaben
            p = subprocess.Popen(["make", "-C", f"levels/level{level_number}", "run"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if level_number == 4 or level_number == 5:
                # Lese Benutzereingaben für Level 4 und 5
                eingabe1 = input("Gib die erste Zahl ein: ") + "\n"
                eingabe2 = input("Gib die zweite Zahl ein: ") + "\n"
                user_input = eingabe1 + eingabe2
                stdout, stderr = p.communicate(input=user_input)
            else:
                stdout, stderr = p.communicate()

            print(stdout)
            if p.returncode != 0:
                print(f"Fehler beim Ausführen von Level {level_number}: {stderr}")

        # Markiere das Level als abgeschlossen
        mark_level_completed(language, level_number)

    except FileNotFoundError:
        print(f"Level {level_number} nicht gefunden.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Make-Befehls: {e}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

def determine_language_for_level(level_number):
    if 1 <= level_number <= 3:
        return "Python"
    elif 4 <= level_number <= 6:
        return "C++"
    elif 7 <= level_number <= 12:
        return "Algorithms"
    elif 13 <= level_number <= 18:
        return "Struktogramme"
    elif 19 <= level_number <= 24:
        return "Projects"
    return "Unknown"

def main():
    progress = load_progress()
    if not progress["player_name"]:
        name = input("Bitte gib deinen Spielernamen ein: ")
        set_player_name(name)
    print("Willkommen bei CodeQuest Terminal Edition!")
    while True:
        print("\n1. Wähle ein Level")
        print("2. Zeige Fortschritt")
        print("3. Beende das Spiel")
        choice = input("Wähle eine Option: ")

        if choice == "1":
            level_number = input("Wähle ein Level: ")
            if level_number.isdigit():
                load_level(int(level_number))
            else:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        elif choice == "2":
            display_progress()
        elif choice == "3":
            break
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
```

## Zusammenfassung

Mit diesen Schritten hast du eine Fortschrittsanzeige und eine Möglichkeit zum Speichern und Laden des Spielerfortschritts in einer JSON-Datei implementiert. Spieler können nun ihren Fortschritt sehen und wissen, welche Levels sie bereits abgeschlossen haben und welche noch ausstehen. Das Skript berücksichtigt Benutzereingaben während der Ausführung der C++-Levels und markiert abgeschlossene Levels im Fortschrittsdatensatz.
