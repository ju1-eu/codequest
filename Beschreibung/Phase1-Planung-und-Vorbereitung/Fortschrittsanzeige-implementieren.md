# Schritt 1: Struktur des Fortschrittsdatensatzes

Zuerst definieren wir die Struktur des JSON-Datensatzes, der den Fortschritt eines Spielers speichert.

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

Erstelle eine Python-Datei `progress.py`, die Funktionen zum Laden und Speichern des Fortschritts enthält.

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

Integriere die Fortschrittsanzeige und das Markieren abgeschlossener Levels in dein Hauptspielskript `game.py`.

```python
import os
from progress import load_progress, save_progress, mark_level_completed, display_progress, set_player_name

def load_level(level_number):
    # Lade die Anweisungen für das Level
    instructions_file = f"levels/level{level_number}/instructions.md"
    if not os.path.exists(instructions_file):
        print(f"Level {level_number} nicht gefunden.")
        return

    with open(instructions_file) as f:
        instructions = f.read()
    print(instructions)

    # Warte auf den Spieler, den Code zu schreiben und zu testen
    input("Drücke Enter, wenn du den Code geschrieben und getestet hast...")

    # Markiere das Level als abgeschlossen
    language = determine_language_for_level(level_number)
    mark_level_completed(language, level_number)

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

Mit diesen Schritten hast du eine Fortschrittsanzeige und eine Möglichkeit zum Speichern und Laden des Spielerfortschritts in einer JSON-Datei implementiert. Spieler können nun ihren Fortschritt sehen und wissen, welche Levels sie bereits abgeschlossen haben und welche noch ausstehen.
