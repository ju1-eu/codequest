# Git-Konfiguration anpassen

Die Warnungen von Git, weisen darauf hin, dass die Zeilenenden in einigen Dateien von CRLF (Carriage Return Line Feed, verwendet unter Windows) zu LF (Line Feed, verwendet unter Unix/Linux und macOS) geändert werden. Dies passiert häufig, wenn du auf verschiedenen Betriebssystemen arbeitest, da diese unterschiedliche Zeilenendungen verwenden.

Um sicherzustellen, dass alle Dateien in deinem Projekt korrekt behandelt werden, kannst du die `.gitattributes`-Datei erweitern, um spezifische Regeln für die verschiedenen Dateitypen wie Markdown (`.md`), Python (`.py`), C++ (`.cpp`), und JSON (`.json`) festzulegen.

1. **Erstelle oder bearbeite die `.gitattributes`-Datei** in deinem Projektverzeichnis:
   ```sh
   touch .gitattributes
   ```

2. **Füge die folgenden Zeilen zu `.gitattributes` hinzu**:
   ```plaintext
   # Set default behavior, in case users don't have core.autocrlf set.
   * text=auto

   # Explicitly declare text files you want to always be normalized and converted to LF in the repository
   *.md text eol=lf
   *.py text eol=lf
   *.cpp text eol=lf
   *.json text eol=lf

   # Declare files that will always have CRLF line endings on checkout.
   *.bat text eol=crlf

   # Declare files that will always have LF line endings on checkout.
   *.sh text eol=lf
   ```

   Diese `.gitattributes`-Datei stellt sicher, dass die angegebenen Dateitypen immer LF-Zeilenendungen im Repository haben.

3. **Setze die Git-Konfiguration, um die Zeilenendungen zu konvertieren**:
   - Auf macOS solltest du die `core.autocrlf`-Einstellung auf `input` setzen, damit Git nur beim Einfügen von Dateien ins Repository die Zeilenendungen in LF konvertiert:
    ```sh
    git config --global core.autocrlf input
    ```

4. **Füge die `.gitattributes`-Datei hinzu und committe sie**:
   ```sh
   git add .gitattributes
   git commit -m "Add .gitattributes to handle line endings for specific file types"
   ```

5. **Normalisiere die Zeilenendungen der Dateien**:
   ```sh
   git add --renormalize .
   git commit -m "Normalize all line endings"
   ```

6. **Überprüfe die Git-Konfiguration**:
   - Stelle sicher, dass die globale und lokale Git-Konfiguration korrekt eingestellt ist:
   ```sh
   git config --global core.eol lf
   git config core.eol lf
   git config core.autocrlf input
   ```
