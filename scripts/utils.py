"""
Die Datei `utils.py` in `scripts/` kann verschiedene Hilfsfunktionen enthalten,
die wiederverwendbaren Code bereitstellen, um die Hauptlogik in deinem Spielskript `game.py`
und anderen Skripten zu unterstützen.

1. **validate_level_number**: Überprüft, ob die eingegebene Levelnummer gültig ist.
2. **format_instructions**: Liest die Anweisungen aus der Datei und gibt sie formatiert zurück.
3. **load_json_file**: Lädt JSON-Daten aus einer Datei.
4. **save_json_file**: Speichert Daten im JSON-Format in eine Datei.
5. **prompt_for_numbers**: Fordert den Benutzer zur Eingabe von Zahlen auf und gibt die eingegebenen Zahlen als Liste zurück.
"""
import os
import json

def validate_level_number(level_number, max_level=24):
    """
    Überprüft, ob die eingegebene Levelnummer gültig ist.
    :param level_number: Die eingegebene Levelnummer
    :param max_level: Die maximale Anzahl an Levels
    :return: True, wenn die Levelnummer gültig ist, sonst False
    """
    if level_number.isdigit():
        level_number = int(level_number)
        return 1 <= level_number <= max_level
    return False

def format_instructions(instructions_path):
    """
    Liest die Anweisungen aus der Datei und gibt sie formatiert zurück.
    :param instructions_path: Der Pfad zur Anweisungsdatei
    :return: Der Inhalt der Anweisungsdatei als String
    """
    try:
        with open(instructions_path, 'r') as f:
            instructions = f.read()
        return instructions
    except FileNotFoundError:
        return "Anweisungen nicht gefunden."

def load_json_file(file_path):
    """
    Lädt JSON-Daten aus einer Datei.
    :param file_path: Der Pfad zur JSON-Datei
    :return: Die geladenen JSON-Daten als Dictionary
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_json_file(file_path, data):
    """
    Speichert Daten im JSON-Format in eine Datei.
    :param file_path: Der Pfad zur JSON-Datei
    :param data: Die zu speichernden Daten
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def prompt_for_numbers(prompt_message, num_prompts=2):
    """
    Fordert den Benutzer zur Eingabe von Zahlen auf.
    :param prompt_message: Die Nachricht, die dem Benutzer angezeigt wird
    :param num_prompts: Die Anzahl der Eingabeaufforderungen
    :return: Eine Liste der eingegebenen Zahlen
    """
    numbers = []
    for i in range(num_prompts):
        while True:
            try:
                number = int(input(f"{prompt_message} ({i + 1}/{num_prompts}): "))
                numbers.append(number)
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
    return numbers
