from random import randint
from collections import namedtuple

class Chromosome:
    def __init__(self, value=None):
        if (value is None):
            self.queenPositions = [randint(0, 7) for i in range(8)] # Array of 4 random integers
        else:
            self.queenPositions = value
        self.probabilityOfBeingChosen = 0
        
        # Compute fitness
        f = Fitness(self)     
        self.fitness = f.getFitness()
    
    # Returns the horizontal length of the board
    # Note: It is assumed that the board is square
    def boardLength(self):
        return len(self.queenPositions)

    # Returns the vertical height of the board
    # Note: It is assumed that the board is square
    def boardHeight(self):
        return self.boardLength()
    
    # Makes Chromosome class printable to console
    def __repr__(self):
        return str(self.queenPositions)

class Fitness:
    def __init__(self, chromosome): 
        self.chromosome = chromosome
        self.collisionCount = self.detectAttacks()

    # Returns the fitness score, which is the sum of all attacks
    def getFitness(self): 
        return self.collisionCount
    
    # Determines how many attacks are possible for each of the queens on the board.
    # Returns the sum of all collisions.
    def detectAttacks(self):
        collisionCount = 0
        for queenColumn in range(len(self.chromosome.queenPositions)):
            collisionCount = collisionCount + self.detectHorizontalAttacks(queenColumn)
            collisionCount = collisionCount + self.detectDiagonalAttacks(queenColumn)
        return collisionCount

    # Determines how many horizontal attacks this individual queen can make. 
    # Returns the number of possible horizontal attacks.
    # col: The column number of the queen being evaluated (Note: there is always exactly one queen in every column)
    def detectHorizontalAttacks(self, col):
        masterQueenPosition = self.chromosome.queenPositions[col]
        collisionCount = 0
        for position in self.chromosome.queenPositions:
            if position == masterQueenPosition:
                collisionCount = collisionCount + 1
        collisionCount = collisionCount - 1 # Subtract 1, becuase the masterQueenPosition was included in collisionCount
        return collisionCount
    
    # Determines how many diagonal attacks this individual queen can make. 
    # Returns the number of possible diagonal attacks.
    # col: The column number of the queen being evaluated (Note: there is always exactly one queen in every column)
    def detectDiagonalAttacks(self, col):
        collisionCount = 0

        # Setup search
        masterQueenPosition = Position(col, self.chromosome.queenPositions[col])

        # Search diagnoally UP and to the RIGHT
        searchPosition = Position(masterQueenPosition.x, masterQueenPosition.y) # Reset search position
        while(searchPosition.x < self.chromosome.boardLength() and searchPosition.y < self.chromosome.boardHeight()):
            if(self.chromosome.queenPositions[searchPosition.x] == searchPosition.y):
                # Check that searchPosition is different from masterQueenPosition
                if((searchPosition.x == masterQueenPosition.x and searchPosition.y == masterQueenPosition.y) is False):
                    collisionCount = collisionCount + 1

            searchPosition.x = searchPosition.x + 1
            searchPosition.y = searchPosition.y + 1
        
        # Search diagnoally DOWN and to the LEFT
        searchPosition = Position(masterQueenPosition.x, masterQueenPosition.y) # Reset search position
        while(searchPosition.x > 0 and searchPosition.y > 0):
            if(self.chromosome.queenPositions[searchPosition.x] == searchPosition.y):
                # Check that searchPosition is different from masterQueenPosition
                if((searchPosition.x == masterQueenPosition.x and searchPosition.y == masterQueenPosition.y) is False):
                    collisionCount = collisionCount + 1

            searchPosition.x = searchPosition.x - 1
            searchPosition.y = searchPosition.y - 1

        # Search diagnoally UP and to the LEFT
        searchPosition = Position(masterQueenPosition.x, masterQueenPosition.y) # Reset search position
        while(searchPosition.x > 0 and searchPosition.y < self.chromosome.boardHeight()):
            if(self.chromosome.queenPositions[searchPosition.x] == searchPosition.y):
                # Check that searchPosition is different from masterQueenPosition
                if((searchPosition.x == masterQueenPosition.x and searchPosition.y == masterQueenPosition.y) is False):
                    collisionCount = collisionCount + 1

            searchPosition.x = searchPosition.x - 1
            searchPosition.y = searchPosition.y + 1

        # Search diagnoally DOWN and to the RIGHT
        searchPosition = Position(masterQueenPosition.x, masterQueenPosition.y) # Reset search position
        while(searchPosition.x < self.chromosome.boardLength() and searchPosition.y > 0):
            if(self.chromosome.queenPositions[searchPosition.x] == searchPosition.y):
                # Check that searchPosition is different from masterQueenPosition
                if((searchPosition.x == masterQueenPosition.x and searchPosition.y == masterQueenPosition.y) is False):
                    collisionCount = collisionCount + 1

            searchPosition.x = searchPosition.x + 1
            searchPosition.y = searchPosition.y - 1
        return collisionCount


# Represents x, y positions on the board
class Position: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Population:
    def __init__(self, size):
        self.generateInitialPopulation(size)
        self.computeProbabilityOfBeingChosen()
        self.populationSize = size
        self.mateCount = int(size / 2) # The number of chromosomes that should mate

    def generateInitialPopulation(self, size):
        self.population = [Chromosome() for i in range(size)] # Array of 8 random chromosomes
    
    def computeProbabilityOfBeingChosen(self):
        fitnessSum = 0 # Sum of all the fitness values in the population
        for chromosome in self.population:
            fitnessSum = fitnessSum + chromosome.fitness
        
        # Set the probablity of being chosen for each chromosome
        for chromosome in self.population:
            # Probability of being chosen = (fitness/fitnessSum) * 100
            chromosome.probabilityOfBeingChosen = (chromosome.fitness / fitnessSum) * 100
    
    # Make the chromosomes mate
    def mate(self):
        matingPairs = self.findMatingPairs()
        children = []
        for pair in matingPairs: 
            c = self.crossover(pair)
            children.append(c[0])
            children.append(c[1])
        print(children)

        # Generate mutations
    
    def mutate(self):
        
    
    # Finds mating pairs. The number of mating pairs found is self.mateCount
    def findMatingPairs(self):
        sortedPopulation = sorted(self.population, key= lambda x: x.probabilityOfBeingChosen, reverse=True)
        mates = []
        for i in range(self.mateCount):
            mates.append((sortedPopulation[i], self.findMate(sortedPopulation)))
        return mates


    # Finds an individual mating pair
    def findMate(self, sortedPopulation):
        # Sort population by probability of mating
        random = randint(0, 100)
        start = 0
        end = 0
        for mate in sortedPopulation:
            end = start + mate.probabilityOfBeingChosen
            if (random >= start and random <= end):
                return mate
            start = end

    def crossover(self, pairs):
        split = randint(0, self.populationSize - 1)
        inverse = pairs[0].boardLength() - split

        FirstHalf = pairs[0].queenPositions[:split]
        SecondHalf = pairs[1].queenPositions[split:]
        child_one = FirstHalf + SecondHalf

        FirstHalf = pairs[1].queenPositions[:inverse]
        SecondHalf = pairs[0].queenPositions[inverse:]

        child_two = FirstHalf + SecondHalf

        return (child_one, child_two)


   # Makes Population class printable to console
    def __repr__(self):
        return str(self.population)


class Runner:
    def generateInitialPopulation(self):
        self.population = Population(10) # Array of 8 random chromosomes
        print(self.population)

# for i in range(10000):
#     c = Chromosome()
#     print(c)
#     # f = Fitness(c)
#     # print("Fitness: ", f.getFitness())
p = Population(10)
p.mate()