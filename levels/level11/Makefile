# Makefile für Level 11

CXX = g++
CXXFLAGS = -Wall -std=c++20
TARGET = task

all: $(TARGET)

$(TARGET): task.cpp
	$(CXX) $(CXXFLAGS) task.cpp -o $(TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)
