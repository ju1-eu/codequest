"""
Jedes Level enthält eine Anleitung (instructions.md), eine Aufgabe (task.py)
und eine Lösung (solution.py). Das Hauptspielskript (game.py) lädt die Level
und zeigt die Anweisungen an.
Ein Testskript (test_levels.py) ermöglicht das Testen der Aufgaben.
"""
import os
import subprocess

def load_level(level_number):
    level_number = int(level_number)  # Konvertiere level_number in eine Ganzzahl
    language = 'python' if level_number <= 3 else 'cpp'

    instructions_path = f"levels/level{level_number}/instructions.md"

    try:
        with open(instructions_path) as f:
            instructions = f.read()
        print(instructions)

        if language == 'python':
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

    except FileNotFoundError:
        print(f"Level {level_number} nicht gefunden.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Make-Befehls: {e}")
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
