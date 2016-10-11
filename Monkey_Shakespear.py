from Population import Population

# Demonstration of using a genetic algorithm to perform a search
#
# setup()
#    # Step 1: The Population 
#    # Create an empty population (an array or ArrayList)
#    # Fill it with DNA encoded objects (pick random values to start)
#
# draw()
#  # Step 1: Selection 
#    # Create an empty mating pool (an empty ArrayList)
#    # For every member of the population, evaluate its fitness based on some criteria / function, 
#      and add it to the mating pool in a manner consistant with its fitness, i.e. the more fit it 
#      is the more times it appears in the mating pool, in order to be more likely picked for reproduction.
#
#  # Step 2: Reproduction Create a new empty population
#    # Fill the new population by executing the following steps:
#       1. Pick two "parent" objects from the mating pool.
#       2. Crossover -- create a "child" object by mating these two parents.
#       3. Mutation -- mutate the child's DNA based on a given probability.
#       4. Add the child object to the new population.
#    # Replace the old population with the new population
#  
#   # Rinse and repeat

  
#class Population:
#    def __init__(self, target, mutation, popmax):
#        

if __name__ == '__main__':
    
    target = 'Genetic'    
    mutation = 0.02
    popmax = 100
    
    
    population = Population ( target, mutation, popmax)

    for i in range (1000): 
        if population.finished == False:
            
            population.calcFitness()
#    Generate mating pool        
            population.naturalSelection()
#       Create next generation
            population.generate()
#       Calculate fitness


            population.evaluate()        
        else:
            break
#    population.evaluate()
#        if population.population.finished == True:
#            break
#   If we found the target phrase, stop

    
        