# Git (Versionskontrollsystem)

## Schritt 1: Git-Repository initialisieren

Zuerst musst du ein Git-Repository für dein Projekt initialisieren.

1. Öffne das Terminal und navigiere zu deinem Projektverzeichnis.

```sh
cd /Users/jan/daten/start/Programmierung/Projekte/codequest
```

2. Initialisiere ein neues Git-Repository.

```sh
git init
```

## Schritt 2: .gitignore-Datei erstellen

Erstelle eine `.gitignore`-Datei, um Dateien und Verzeichnisse auszuschließen, die nicht versioniert werden sollen, z.B. Kompilierungsartefakte und temporäre Dateien.

**Datei: .gitignore**

```plaintext
# Python Bytecode
__pycache__/
*.pyc

# C++ Build Files
levels/level*/task.out

# VSCode Settings
.vscode/

# Other
*.o
*.exe
*.log
```

## Schritt 3: Erste Dateien hinzufügen und Commit erstellen

1. Füge alle relevanten Dateien zum Repository hinzu.

```sh
git add .
```

2. Erstelle deinen ersten Commit.

```sh
git commit -m "Initial commit: Projektstruktur und erste Level hinzugefügt"
```

## Schritt 4: Branching und Feature-Entwicklung

Git-Branching ermöglicht es dir, neue Features oder Änderungen in isolierten Umgebungen zu entwickeln, bevor du sie in den Hauptzweig integrierst.

1. Erstelle einen neuen Branch für ein neues Feature oder eine Änderung.

```sh
git checkout -b feature/level4-6
```

2. Entwickle dein Feature oder nimm Änderungen vor.

3. Füge die Änderungen hinzu und erstelle einen Commit.

```sh
git add .
git commit -m "Feature: Level 4-6 hinzugefügt"
```

4. Wechsel zurück zum Hauptzweig und integriere die Änderungen.

```sh
git checkout main
git merge feature/level4-6
```

5. Lösche den Feature-Branch, wenn er nicht mehr benötigt wird.

```sh
git branch -d feature/level4-6
```

## Schritt 5: Zusammenarbeit mit anderen (Remote Repository)

Um mit anderen Entwicklern zusammenzuarbeiten oder deine Arbeit zu sichern, kannst du ein Remote-Repository (z.B. auf GitHub) verwenden.

1. Erstelle ein Repository auf GitHub (oder einer anderen Plattform).

2. Füge das Remote-Repository zu deinem lokalen Repository hinzu.

```sh
git remote add origin https://github.com/username/codequest.git
```

3. Schiebe deinen lokalen Code zum Remote-Repository.

```sh
git push -u origin main
```

## Schritt 6: Änderungen von anderen abrufen und integrieren

Wenn du mit anderen zusammenarbeitest, möchtest du regelmäßig Änderungen vom Remote-Repository abrufen und integrieren.

1. Hole die neuesten Änderungen vom Remote-Repository.

```sh
git pull origin main
```

## Schritt 7: Fortgeschrittene Techniken

1. **Stash**: Temporäre Änderungen speichern und später anwenden.

```sh
git stash
# Änderungen anwenden
git stash pop
```

2. **Rebase**: Änderungen auf einen neuen Basis-Commit anwenden.

```sh
git rebase main
```

3. **Tags**: Versionsmarkierungen erstellen.

```sh
git tag -a v1.0 -m "Version 1.0"
git push origin v1.0
```

## Schritt 8: Konflikte lösen

Bei der Zusammenführung von Branches können Konflikte auftreten. Git zeigt an, wo die Konflikte sind, und du musst diese manuell lösen.

1. Öffne die Dateien mit Konflikten.
2. Suche nach den Markierungen `<<<<<<<`, `=======` und `>>>>>>>` und wähle die gewünschten Änderungen.
3. Entferne die Markierungen und speichere die Datei.
4. Füge die Datei erneut hinzu und erstelle einen Commit.

```sh
git add conflict_file.py
git commit -m "Konflikte gelöst"
```

## Zusammenfassung

Durch die Nutzung von Git in deinem Projekt kannst du:

- Änderungen verfolgen und die Entwicklungsgeschichte dokumentieren.
- In isolierten Branches neue Features entwickeln.
- Effizient mit anderen Entwicklern zusammenarbeiten.
- Änderungen und Konflikte leicht verwalten.
