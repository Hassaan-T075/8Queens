# 8-Queens Problem Solver with Genetic Algorithm

This repository contains an implementation of a genetic algorithm to solve the classic 8-Queens problem. The 8-Queens problem involves placing eight queens on an 8x8 chessboard in such a way that no two queens threaten each other. The genetic algorithm approach offers an efficient and scalable solution to this combinatorial problem.

## Problem Description

The 8-Queens problem requires finding a configuration of eight queens on an 8x8 chessboard where no two queens can attack each other. In chess, queens can move horizontally, vertically, and diagonally. Therefore, a solution to the 8-Queens problem ensures that no two queens share the same row, column, or diagonal.

## Genetic Algorithm Solution

The genetic algorithm is a search heuristic inspired by the process of natural selection. This implementation utilizes the genetic algorithm to find an optimal or near-optimal solution to the 8-Queens problem. The algorithm consists of the following steps:

1. **Initialization**: Generate an initial population of chessboard configurations.
2. **Fitness Evaluation**: Calculate the fitness of each configuration based on the number of conflicts (queens threatening each other).
3. **Selection**: Select parent configurations from the population based on their fitness.
4. **Crossover**: Create offspring by combining the selected parent configurations.
5. **Mutation**: Randomly mutate the offspring to introduce diversity.
6. **Replacement**: Replace some individuals in the population with the offspring.
7. **Termination**: Repeat steps 2-6 until a termination condition is met (e.g., finding a solution or reaching a maximum number of iterations).

## Usage

To run the program, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Clone this repository: `git clone https://github.com/your-username/8-queens-genetic-algorithm.git`
3. Navigate to the project directory: `cd 8-queens-genetic-algorithm`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the program: `python main.py`

## Results

The algorithm will output the best solution found, which represents a valid placement of eight queens on the chessboard. Additionally, the program generates a visualization of the final solution, highlighting the queen positions on the board.
