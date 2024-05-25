import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    language = determine_language_for_level(level)
    file_extension = 'py' if language == "Python" else 'cpp'

    if file_extension == 'py':
        command = ["python", f"levels/level{level}/task.py"]
        if level in [1, 2]:  # Levels, die Benutzereingaben erfordern
            input_data = "2\n3\n"  # Beispiel-Eingaben
            result = subprocess.run(command, input=input_data, capture_output=True, text=True, timeout=300)  # Timeout erhöht auf 300 Sekunden
        else:
            result = subprocess.run(command, capture_output=True, text=True, timeout=300)  # Timeout erhöht auf 300 Sekunden
    else:
        print(f"Führe 'make clean' für Level {level} aus...")
        clean_result = subprocess.run(["make", "-C", f"levels/level{level}", "clean"], capture_output=True, text=True)
        print(f"Ausgabe von 'make clean': {clean_result.stdout}")
        if clean_result.returncode != 0:
            print(f"Fehler bei 'make clean': {clean_result.stderr}")
            return False

        print(f"Führe 'make' für Level {level} aus...")
        make_result = subprocess.run(["make", "-C", f"levels/level{level}"], capture_output=True, text=True)
        print(f"Ausgabe von 'make': {make_result.stdout}")
        if make_result.returncode != 0:
            print(f"Fehler bei 'make': {make_result.stderr}")
            return False

        print(f"Führe 'make run' für Level {level} aus...")
        command = ["make", "-C", f"levels/level{level}", "run"]

        if level in [4, 5]:  # Levels, die Benutzereingaben erfordern
            input_data = "2\n3\n"  # Beispiel-Eingaben
            result = subprocess.run(command, input=input_data, capture_output=True, text=True, timeout=300)  # Timeout erhöht auf 300 Sekunden
        else:
            result = subprocess.run(command, capture_output=True, text=True, timeout=300)  # Timeout erhöht auf 300 Sekunden

    print(f"Ausgabe von Level {level}:\n{result.stdout}")
    if result.returncode != 0:
        print(f"Fehler beim Ausführen von Level {level}: {result.stderr}")

    if level >= 7:  # Auch die Python-Dateien für Levels ab 7 ausführen
        command = ["python", f"levels/level{level}/task.py"]
        print(f"Ausgabe von Python für Level {level}:")
        result = subprocess.run(command, capture_output=True, text=True, timeout=300)  # Timeout erhöht auf 300 Sekunden
        print(result.stdout)
        if result.returncode != 0:
            print(f"Fehler beim Ausführen von Python für Level {level}: {result.stderr}")

    return result.returncode == 0

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
    for level in range(1, 13):
        if not run_test(level):
            print(f"Level {level} Test fehlgeschlagen.")
        else:
            print(f"Level {level} Test erfolgreich.")

if __name__ == "__main__":
    main()
