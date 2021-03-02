import random
import numpy as np

generation = 0;

def generateInitialPopulation():

    random.randint(0,8)
    # Population of size 10
    population = [0]*100
    # chromosome array with 8 genes(Position of the Queen)
    chromosomes = [0]*8

    #loops N (Size of population times)
    for x in range(0,100):
        #Loops 8 times to randomly assign genes (Queens placements) to chromosomes
        for i in range(0,8):
            chromosomes[i] = random.randint(1,8)
        #Add chromosome with 8 genes to the population
        population[x] = chromosomes
        #reset chromosome array to create new random chromosome
        chromosomes = [0] * 8;

    generateBoards(population)


def generateBoards(population):

    #Loops 10 times (size of population)
    for x in range (len(population)):

        #First chromosome in population
        chromosome = population[x]
        #print(len(chromosome))

        #making 2d array using numpy
        size = (8,8)
        board = np.zeros(size, dtype=int)

        #makes the board, takes the value of the chromo some at first index, puts in it that column on the board, and goes the next
        #Since only 1 queen is on the column we can just go 1-8 on rows

        for x in range(0, len(chromosome)):
            #print("The gene value of the chromosome is : " + str((chromosome[x]) -1 ))
            board[(chromosome[x] -1)][x] = 1

        #print(chromosome)
        #print(board)

        fitness(chromosome,board)

    #for x in range(0, 10):
        #print(population[x])

def fitness(chromosome, board):
    print("fitness")


def crossover(): #is this was the crossover function is meant to do?

    print("crossover")

    c1 = [7,3,1,8,3,4,5,6]
    c2 = [1,8,3,2,7,5,5,2]

    split = random.randint(0,7)
    inverse = 7 - split

    FirstHalf = c1[:split]
    SecondHalf = c2[split:]

    child_one = FirstHalf + SecondHalf

    FirstHalf = c2[:inverse]
    SecondHalf = c1[inverse:]

    child_two = FirstHalf + SecondHalf

    print(child_one)
    print(child_two)

    for x in range(0,20):

        mutationoptions = [0,1] #0 for no mutaion, 1 for mutation
        chance = [0.8,0.2]
        choice = random.choices(mutationoptions,chance)

        if choice[0] == 1:

            print("Mutated")
            child_one = mutation(child_one)
            child_two = mutation(child_two)

            print(child_one)
            print(child_two)

        #print(choice)



def mutation(child):

    swapIndex = random.randint(0, 7)
    inverse = 7 - swapIndex

    mutated = child

    print("Swap Index: " + str(swapIndex))
    print("Inverse: " + str(inverse))

    temp = mutated[swapIndex]
    mutated[swapIndex] = mutated[inverse]
    mutated[inverse] = temp

    return mutated;

if __name__ == '__main__':

    crossover()
    #generateInitialPopulation()

