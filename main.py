import time as t
import random

# U, R, D, UPPER-R, LOWER-R
dRow = [-1, 0, 1, -1, 1]
dCol = [0, 1, 0, 1, 1]

#checks if block being accessed lies within bounds
def isValid(row, col):

    # if cell is out of bounds
    if (row < 0 or col < 0 or row >= 8 or col >= 8):
        return False

    # else
    return True


def gen():

    pop = [
        # [3, 2, 7, 5, 2, 4, 1, 1],
        # [2, 4, 7, 4, 8, 5, 5, 2],
        # [3, 2, 5, 4, 3, 2, 1, 3],
        # [2, 4, 6, 8, 3, 1, 7, 5],
        random.sample(range(1, 9), 8),
        random.sample(range(1, 9), 8),
        random.sample(range(1, 9), 8),
        random.sample(range(1, 9), 8)
    ]

    return pop


def fitness(board, chrom):  # computes fitness of a chromosome
    
    #max fitness can be 28
    f = 28

    #places queens on board
    for i in range(len(chrom)):
        board[8-chrom[i]][i] = 1

    for i in range(0, 8):
        for j in range(0, 5): # do for all queens
            x = 8 - chrom[i]
            y = i
            while 1: #keeps moving forward in a direction until corner is reached
                if isValid(x + dRow[j], y + dCol[j]):
                    x = x + dRow[j]
                    y = y + dCol[j]
                    if board[x][y] == 1:
                        f -= 1
                else:
                    break
    return f


def start_GA(p):

    print("------------------------------------\n")
    print(f"Initial Population : {p}")

    f = [0, 0, 0, 0]  # fitness array

    for i in range(0, 4):
        board = [[0 for i in range(8)] for j in range(8)]
        f[i] = fitness(board, p[i]) # compute and store fitness for each chromosome in population
        if f[i] == 28:
            print("Solution Found")
            return [p[i]]

    print(f"Fitness : {f}")
    return roulette(p, f)


def roulette(p, f):

    # select parents
    parents = [[], [], [], []]
    sum_of_f = 0

    # Roulette Wheel
    for i in range(len(f)):
        sum_of_f = sum_of_f + f[i]

    print(f"Sum of Fitnesses : {sum_of_f}\n")

    for j in range(len(p)):
        r = random.randint(0, sum_of_f)
        print("Random number for Roulette Wheel is " + str(r))

        selection_val = 0
        for i in range(len(f)):
            selection_val = selection_val + f[i]
            if selection_val >= r:
                parents[j] = p[i]
                break

    print(f"\nSelected Parents : {parents}")
    return crossover(parents)


def crossover(parents):

    new_population = [[], [], [], []]

    cross_point_1 = random.randint(0, 8)
    cross_point_2 = random.randint(0, 8)

    print(f"Cross over point 1 : {cross_point_1}")
    # crossover parents 1 and 3
    new_population[0] = parents[0][:cross_point_1] + parents[2][cross_point_1:]
    new_population[1] = parents[2][:cross_point_1] + parents[0][cross_point_1:]

    print(f"Cross over point 2 : {cross_point_2}")
    # crossover parents 2 and 4
    new_population[2] = parents[1][:cross_point_2] + parents[3][cross_point_2:]
    new_population[3] = parents[3][:cross_point_2] + parents[1][cross_point_2:]

    print(f"New Population : {new_population}")

    f = [0, 0, 0, 0]  # fitness array

    for i in range(0, 4): # this will be used in mutation
        board = [[0 for i in range(8)] for j in range(8)]
        f[i] = fitness(board, new_population[i]) # compute fitness of new generated population

    return mutation(new_population, f)


def mutation(pop, f):

    max_index = f.index(max(f))

    for i in range(len(pop)):
        if i != max_index: # do not mutate chromosome with max fitness
            r = random.randint(1, 8)
            s = random.randint(1,8)
            
            a = pop[i][r - 1]
            pop [i][r - 1] = pop[i][s - 1]
            pop[i][s - 1] = a


    # for i in range(len(pop)):
    #     if i != max_index:
    #         r = random.randint(1, 8)
    #         pop[i][r - 1] = r

    print(f"Mutated Population : {pop}\n")
    return pop


#driver code
pop = gen()

while 1:
    t.sleep(0.5)
    pop = start_GA(pop)
    if len(pop) == 1: # when solution is found so only solution chromosome is returned, so len will be 1
        break

print(f"\nSolution Chromosome : {pop[0]}")