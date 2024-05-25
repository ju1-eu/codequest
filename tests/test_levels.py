import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    file_extension = 'py' if level <= 3 else 'cpp'

    if file_extension == 'py':
        command = ["python", f"levels/level{level}/task.py"]
        # Simuliere Eingaben für die Python-Levels
        input_data = "2\n3\n" if level == 1 else "4\n5\n"
        result = subprocess.run(command, input=input_data, capture_output=True, text=True, timeout=60)  # Timeout erhöht
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

        if level == 4:
            input_data = "2\n3\n"  # Simulierte Eingaben für Level 4
        elif level == 5:
            input_data = "2\n3\n"  # Simulierte Eingaben für Level 5
        else:
            input_data = None  # Keine Eingaben für Level 6 und darüber

        if input_data:
            result = subprocess.run(command, input=input_data, capture_output=True, text=True, timeout=60)  # Timeout erhöht
        else:
            result = subprocess.run(command, capture_output=True, text=True, timeout=60)  # Timeout erhöht

    print(f"Ausgabe von Level {level}:\n{result.stdout}")
    if result.returncode != 0:
        print(f"Fehler beim Ausführen von Level {level}: {result.stderr}")
    return result.returncode == 0

def main():
    for level in range(1, 7):
        if not run_test(level):
            print(f"Level {level} Test fehlgeschlagen.")
        else:
            print(f"Level {level} Test erfolgreich.")

if __name__ == "__main__":
    main()
