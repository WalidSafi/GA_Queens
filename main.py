from random import randint

class Chromosome:
    def __init__(self):
        self.queenPositions = [randint(0, 8) for i in range(8)] # Array of 8 random integers
    
    # Makes Chromosome class printable to console
    def __repr__(self):
        return str(self.queenPositions)

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

r = Runner()
r.generateInitialPopulation()
