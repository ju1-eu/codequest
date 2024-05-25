import subprocess
import os

def run_test(level):
    print(f"Teste Level {level}")
    file_extension = 'py' if level <= 3 else 'cpp'

    if file_extension == 'py':
        command = ["python", f"levels/level{level}/task.py"]
        # Simuliere Eingaben für die Python-Levels
        input_data = "2\n3\n" if level == 1 else "4\n5\n"
        result = subprocess.run(command, input=input_data, capture_output=True, text=True, timeout=20)
    else:
        subprocess.run(["make", "-C", f"levels/level{level}", "clean"])
        command = ["make", "-C", f"levels/level{level}", "run"]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)

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
