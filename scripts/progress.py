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
