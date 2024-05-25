# Makefile for Level 13-18

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -std=c++20

# Target executables
TARGETS = task

# Source files
SRCS = task.cpp

# Object files
OBJS = $(SRCS:.cpp=.o)

# Default target
all: $(TARGETS)

$(TARGETS): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Clean up
clean:
	rm -f $(TARGETS) $(OBJS)

# Run the program
run: $(TARGETS)
	./$(TARGETS)
