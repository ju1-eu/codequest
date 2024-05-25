# Level 1-3: Grundlagen von Python

**Thema**: Syntax, Variablen, einfache Datentypen, Ein- und Ausgabe

## Level 1: Grundlagen von Python

- **Thema**: Variablen und Datentypen
- **Ziel**: Verständnis der grundlegenden Datentypen und Variablenzuweisung in Python.

**Inhalte**:

- **Syntax**: Einführung in die grundlegende Syntax von Python.
- **Variablen**: Was sind Variablen und wie werden sie in Python verwendet?
- **Datentypen**: Einfache Datentypen wie `int`, `float`, `str`.

**Beispielaufgabe**:

- Schreibe ein Programm, das zwei Zahlen einliest, sie addiert und das Ergebnis ausgibt.

**Beispielcode**:

```python
# Eingabe der ersten Zahl
zahl1 = input("Gib die erste Zahl ein: ")
# Eingabe der zweiten Zahl
zahl2 = input("Gib die zweite Zahl ein: ")

# Konvertierung der Eingaben in Ganzzahlen
zahl1 = int(zahl1)
zahl2 = int(zahl2)

# Berechnung der Summe
summe = zahl1 + zahl2

# Ausgabe des Ergebnisses
print("Die Summe ist:", summe)
```

## Level 2: Einfache mathematische Operationen und Ausgaben

- **Thema**: Mathematische Operationen und Ausgaben mit `print()`
- **Ziel**: Erlernen von mathematischen Operationen und der Nutzung der `print()` Funktion.

**Inhalte**:

- **Mathematische Operationen**: Addition, Subtraktion, Multiplikation, Division.
- **Ein- und Ausgabe**: Nutzung von `input()` und `print()`.

**Beispielaufgabe**:

- Schreibe ein Programm, das zwei Zahlen einliest, sie multipliziert und das Ergebnis ausgibt.

**Beispielcode**:

```python
# Eingabe der ersten Zahl
zahl1 = input("Gib die erste Zahl ein: ")
# Eingabe der zweiten Zahl
zahl2 = input("Gib die zweite Zahl ein: ")

# Konvertierung der Eingaben in Ganzzahlen
zahl1 = int(zahl1)
zahl2 = int(zahl2)

# Berechnung des Produkts
produkt = zahl1 * zahl2

# Ausgabe des Ergebnisses
print("Das Produkt ist:", produkt)
```

## Level 3: Bedingte Anweisungen und Schleifen

- **Thema**: `if`-Anweisungen und `for`-Schleifen
- **Ziel**: Einführung in Kontrollstrukturen.

**Inhalte**:

- **Bedingte Anweisungen**: `if`, `else if`, `else`.
- **Schleifen**: `for`-Schleifen.

**Beispielaufgabe**:

- Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.

**Beispielcode**:

```python
# Schleife über die Zahlen von 1 bis 10
for zahl in range(1, 11):
    # Bedingte Anweisung zur Überprüfung, ob die Zahl gerade ist
    if zahl % 2 == 0:
        print(zahl, "ist gerade.")
    else:
        print(zahl, "ist ungerade.")
```

## Zusammenfassung der Level 1-3

**Level 1**: Einführung in Variablen und Datentypen

- **Thema**: Variablen und einfache Datentypen (`int`, `float`, `str`).
- **Ziel**: Verständnis der Variablenzuweisung und der grundlegenden Datentypen.
- **Aufgabe**: Programm zur Addition zweier Zahlen.

**Level 2**: Einfache mathematische Operationen und Ausgaben

- **Thema**: Mathematische Operationen und `print()` Funktion.
- **Ziel**: Erlernen mathematischer Operationen und der Ausgabe von Ergebnissen.
- **Aufgabe**: Programm zur Multiplikation zweier Zahlen.

**Level 3**: Bedingte Anweisungen und Schleifen

- **Thema**: `if`-Anweisungen und `for`-Schleifen.
- **Ziel**: Einführung in Kontrollstrukturen.
- **Aufgabe**: Programm zur Ausgabe der Zahlen von 1 bis 10 und Bestimmung, ob sie gerade oder ungerade sind.
