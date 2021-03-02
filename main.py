from random import randint

class Chromosome:
    def __init__(self):
        self.queenPositions = [randint(0, 8) for i in range(8)] # Array of 8 random integers
    
    # Makes Chromosome class printable to console
    def __repr__(self):
        return str(self.queenPositions)

class Fitness:
    def __init__(self, chromosome): 
        self.chromosome = chromosome

    # Determines whether any horizontal attacks are possible for any queens on the board.
    # Returns the number of collisions detected
    # col: There is always exactly one queen in every column. col is the column number of the queen being checked for collisions.
    def detectHorizontalAttacks(self, col):
        masterQueenPosition = self.chromosome.queenPositions[col]
        collisionCount = 0
        for position in self.chromosome.queenPositions:
            if position == masterQueenPosition:
                collisionCount = collisionCount + 1
        collisionCount = collisionCount - 1 # Subtract 1, becuase the masterQueenPosition was included in collisionCount
        return collisionCount

class Population:
    def __init__(self, size):
        self.generateInitialPopulation(size)

    def generateInitialPopulation(self, size):
        self.population = [Chromosome() for i in range(size)] # Array of 8 random chromosomes

   # Makes Population class printable to console
    def __repr__(self):
        return str(self.population)


class Runner:
    def generateInitialPopulation(self):
        self.population = Population(10) # Array of 8 random chromosomes
        print(self.population)

c = Chromosome()
print(c)
f = Fitness(c)
print(f.detectHorizontalAttacks(0))