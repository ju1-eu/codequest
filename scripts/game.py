import os
import subprocess
from progress import load_progress, save_progress, mark_level_completed, display_progress, set_player_name
from utils import validate_level_number, format_instructions, prompt_for_numbers

def load_level(level_number):
    level_number = int(level_number)  # Konvertiere level_number in eine Ganzzahl
    instructions_path = f"levels/level{level_number}/instructions.md"

    try:
        instructions = format_instructions(instructions_path)
        print(instructions)

        if 1 <= level_number <= 3:  # Python-Levels 1-3
            task_path = f"levels/level{level_number}/task.py"
            if level_number in [1, 2]:  # Levels, die Benutzereingaben erfordern
                print("Bitte geben Sie zwei Zahlen ein:")
                input_data = input("Erste Zahl: ") + "\n" + input("Zweite Zahl: ") + "\n"
                subprocess.run(["python", task_path], input=input_data, text=True)
            else:
                os.system(f"python {task_path}")
            mark_level_completed("Python", level_number)

        elif 4 <= level_number <= 6:  # C++-Levels 4-6
            print(f"Führe 'make clean' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "clean"], check=True)

            print(f"Führe 'make' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}"], check=True)

            print(f"Führe 'make run' für Level {level_number} aus...")
            p = subprocess.Popen(["make", "-C", f"levels/level{level_number}", "run"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if level_number in [4, 5]:  # Levels, die Benutzereingaben erfordern
                print("Bitte geben Sie zwei Zahlen ein:")
                input_data = input("Erste Zahl: ") + "\n" + input("Zweite Zahl: ") + "\n"
                stdout, stderr = p.communicate(input=input_data)
            else:
                stdout, stderr = p.communicate()

            print(stdout)
            if p.returncode != 0:
                print(f"Fehler beim Ausführen von Level {level_number}: {stderr}")
            else:
                mark_level_completed("C++", level_number)

        elif 7 <= level_number <= 12:  # Python und C++ für Levels 7-12
            task_path_py = f"levels/level{level_number}/task.py"
            print(f"Ausgabe von Python für Level {level_number}:")
            os.system(f"python {task_path_py}")

            print(f"Führe 'make clean' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "clean"], check=True)

            print(f"Führe 'make' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}"], check=True)

            print(f"Ausgabe von C++ für Level {level_number}:")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "run"], check=True)
            mark_level_completed("Algorithms", level_number)

        elif 13 <= level_number <= 18:  # Struktogramme und Best Practices
            task_path_py = f"levels/level{level_number}/task.py"
            task_path_cpp = f"levels/level{level_number}/task.cpp"
            print(f"Ausgabe von Python für Level {level_number}:")
            os.system(f"python {task_path_py}")

            print(f"Führe 'make clean' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "clean"], check=True)

            print(f"Führe 'make' für Level {level_number} aus...")
            subprocess.run(["make", "-C", f"levels/level{level_number}"], check=True)

            print(f"Ausgabe von C++ für Level {level_number}:")
            subprocess.run(["make", "-C", f"levels/level{level_number}", "run"], check=True)
            mark_level_completed("Struktogramme", level_number)

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
            if validate_level_number(level_number):
                load_level(int(level_number))
            else:
                print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 24 ein.")
        elif choice == "2":
            display_progress()
        elif choice == "3":
            break
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
