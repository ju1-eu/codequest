# Aufgabe: Schreibe ein Programm, das die Zahlen von 1 bis 10 ausgibt und anzeigt, ob jede Zahl gerade oder ungerade ist.
# Dein Code beginnt hier.

# Schleife über die Zahlen von 1 bis 10
for zahl in range(1, 11):
    # Bedingte Anweisung zur Überprüfung, ob die Zahl gerade ist
    if zahl % 2 == 0:
        print(zahl, "ist gerade.")
    else:
        print(zahl, "ist ungerade.")
