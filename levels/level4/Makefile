# Makefile für Level 4

# Compiler und Compiler-Flags
CXX = g++
CXXFLAGS = -Wall -std=c++20

# Zieldatei
TARGET = task

# Standardziel
all: $(TARGET)

# Regel zur Kompilierung
$(TARGET): task.cpp
	$(CXX) $(CXXFLAGS) task.cpp -o $(TARGET)

# Regel zur Ausführung
run: $(TARGET)
	./$(TARGET)

# Regel zum Löschen der erzeugten Dateien
clean:
	rm -f $(TARGET)