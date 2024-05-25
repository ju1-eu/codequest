# Git Begriffe

### Git Stash

**Definition:**
`git stash` ist ein Befehl in Git, der es dir ermöglicht, deine aktuellen Änderungen (sowohl gestaged als auch ungestaged) temporär zu speichern, ohne sie zu committen. Diese Änderungen werden in einem sogenannten "Stash" abgelegt und du kannst später entscheiden, wann du diese Änderungen wiederherstellen möchtest.

**Anwendung:**
- Wenn du an einer Funktion arbeitest und plötzlich etwas Dringendes bearbeiten musst, das auf einem sauberen Arbeitszweig basiert.
- Wenn du deine Arbeit an einem Feature fortsetzen möchtest, ohne einen Zwischen-Commit zu erstellen.

**Beispiel:**

```sh
# Speichere aktuelle Änderungen im Stash
git stash

# Später: Hole die Änderungen wieder hervor
git stash pop
```

### Git Rebase

**Definition:**
`git rebase` ist ein Befehl in Git, der es dir ermöglicht, die Basis deines aktuellen Zweigs auf einen neuen Basis-Commit zu verschieben. Das bedeutet, dass die Änderungen, die auf deinem aktuellen Zweig gemacht wurden, "neu abgespielt" werden auf einem anderen Commit.

**Anwendung:**
- Um eine saubere und lineare Historie zu erstellen, die einfacher zu lesen ist.
- Wenn du Feature-Zweige mit dem Hauptzweig synchronisieren möchtest, bevor du sie in den Hauptzweig integrierst.

**Beispiel:**

```sh
# Rebase den aktuellen Zweig auf den main-Zweig
git rebase main
```

### Unterschied zwischen Stash und Rebase

- `git stash` speichert temporär deine Änderungen, ohne sie in die Commit-Historie aufzunehmen. Es ist nützlich für kurzfristige Kontextwechsel.
- `git rebase` ändert die Commit-Historie, indem es die Basis eines Zweigs auf einen neuen Commit verschiebt. Es wird verwendet, um die Historie zu bereinigen und um sicherzustellen, dass Änderungen auf den neuesten Stand gebracht werden.

### Zusammenfassung

- **Git Stash:** Temporäres Speichern und Wiederherstellen von Änderungen.
- **Git Rebase:** Ändern der Basis eines Zweigs, um eine saubere und lineare Historie zu erstellen.
