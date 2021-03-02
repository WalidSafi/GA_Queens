import random
import numpy as np


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

        print("\n")
        print(chromosome)
        print(board)

    #for x in range(0, 10):
        #print(population[x])

def crossover(): #is this was the crossover function is meant to do?

    print("crossover")

    population1 = [1,2,3,4,5,6,7,8]
    population2 = [8,7,6,5,4,3,2,1]

    split = 4

    popone = population1[:split]
    poptwo = population2[split:]

    print(popone)
    print(poptwo)

    chromosome = popone + poptwo
    print(chromosome)

def mutation():

    mutationchance = 0.10
    print("Mutation")

if __name__ == '__main__':

    crossover()
    #generateInitialPopulation()

