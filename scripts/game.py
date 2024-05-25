"""
Jedes Level enthält eine Anleitung (instructions.md), eine Aufgabe (task.py)
und eine Lösung (solution.py). Das Hauptspielskript (game.py) lädt die Level
und zeigt die Anweisungen an.
Ein Testskript (test_levels.py) ermöglicht das Testen der Aufgaben.
"""
import os

def load_level(level_number):
    level_number = int(level_number)  # Konvertiere level_number in eine Ganzzahl
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
